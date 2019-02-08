// This code is heavily inspired by:
// https://github.com/twitchtv/twirp-ruby/blob/master/protoc-gen-twirp_ruby/main.go
// which is licensed under the Apache License, Version 2.0.

package main

import (
	"bytes"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"strings"

	// "unicode"

	"github.com/golang/protobuf/proto"
	"github.com/golang/protobuf/protoc-gen-go/descriptor"
	plugin "github.com/golang/protobuf/protoc-gen-go/plugin"
)

func main() {
	genReq := readGenRequest(os.Stdin)
	g := &generator{version: Version, genReq: genReq}
	genResp := g.Generate()
	writeGenResponse(os.Stdout, genResp)
}

type generator struct {
	version string
	genReq  *plugin.CodeGeneratorRequest
}

func (g *generator) Generate() *plugin.CodeGeneratorResponse {
	resp := new(plugin.CodeGeneratorResponse)

	for _, f := range g.protoFilesToGenerate() {
		twirpFileName := packageFileName(filePath(f)) + "PB.hs"

		haskellCode := g.generateHaskellCode(f)
		respFile := &plugin.CodeGeneratorResponse_File{
			Name:    proto.String(twirpFileName),
			Content: proto.String(haskellCode),
		}
		resp.File = append(resp.File, respFile)
	}

	return resp
}

func (g *generator) generateHaskellCode(file *descriptor.FileDescriptorProto) string {
	b := new(bytes.Buffer)
	print(b, "-- Code generated by protoc-gen-haskell %s, DO NOT EDIT.", g.version)
	print(b, "{-# LANGUAGE DerivingVia, DeriveAnyClass, DuplicateRecordFields #-}")
	print(b, "{-# OPTIONS_GHC -Wno-unused-imports #-}")

	pkgName := file.GetPackage()
	moduleName := toModuleName(pkgName)
	print(b, "module %sPB where", moduleName)
	print(b, "")

	print(b, "import Data.Aeson")
	print(b, "import Data.ByteString (ByteString)")
	print(b, "import Data.Fixed (Fixed)")
	print(b, "import Data.Int")
	print(b, "import Data.Text (Text)")
	print(b, "import Data.Word")
	print(b, "import GHC.Generics")
	print(b, "import Proto3.Suite")

	for _, message := range file.MessageType {
		generateMessage(b, message)
	}
	for _, enum := range file.EnumType {
		generateEnum(b, enum)
	}

	return b.String()
}

func generateMessage(b *bytes.Buffer, message *descriptor.DescriptorProto) {
	oneofs := []string{}
	for _, oneof := range message.OneofDecl {
		generateOneof(b, message, oneof)
		oneofs = append(oneofs, oneof.GetName())
	}

	n := message.GetName()
	print(b, "")
	print(b, "data %s = %s", n, n)
	first := true
	for _, field := range message.Field {
		n := toHaskellFieldName(field.GetName())
		t := toType(field)
		if field.OneofIndex == nil {
			sep := ","
			if first {
				sep = "{"
			}
			print(b, "  %s %s :: %s", sep, n, t)
			first = false
		}
	}
	for _, n := range oneofs {
		t := fmt.Sprintf("%s%s", strings.Title(message.GetName()), strings.Title(n))
		sep := ","
		if first {
			sep = "{"
		}
		print(b, "  %s %s :: Maybe %s", sep, n, t)
		first = false
	}
	print(b, "  } deriving stock (Eq, Ord, Show, Generic)")
	print(b, "    deriving anyclass (Message, Named, FromJSON, ToJSON)")

	for _, nested := range message.NestedType {
		generateMessage(b, nested)
	}
	for _, enum := range message.EnumType {
		generateEnum(b, enum)
	}
}

func generateOneof(b *bytes.Buffer, message *descriptor.DescriptorProto, oneof *descriptor.OneofDescriptorProto) {
	oneofName := oneof.GetName()
	n := fmt.Sprintf("%s%s", strings.Title(message.GetName()), strings.Title(oneofName))
	print(b, "")
	print(b, "data %s", n)
	first := true
	for _, field := range message.Field {
		fieldName := toHaskellFieldName(field.GetName())
		n := enumToHaskellSumType(field.GetName())
		t := toType(field)
		if field.OneofIndex != nil {
			sep := "|"
			if first {
				sep = "="
			}
			print(b, "  %s %s { %s :: %s }", sep, n, fieldName, t)
			first = false
		}
	}
	print(b, "  deriving stock (Eq, Ord, Show, Generic)")
	print(b, "  deriving anyclass (Message, Named, FromJSON, ToJSON)")
}

func generateEnum(b *bytes.Buffer, enum *descriptor.EnumDescriptorProto) {
	n := enum.GetName()
	print(b, "")
	print(b, "data %s", n)
	first := true
	def := ""
	for _, value := range enum.Value {
		v := enumToHaskellSumType(value.GetName())
		sep := "|"
		if first {
			sep = "="
			def = v
		}
		print(b, "  %s %s", sep, v)
		first = false
	}
	print(b, "  deriving stock (Eq, Ord, Show, Enum, Bounded, Generic)")
	print(b, "  deriving anyclass (Named, MessageField, FromJSON, ToJSON)")
	print(b, "  deriving Primitive via PrimitiveEnum %s", n)
	if def != "" {
		print(b, "instance HasDefault %s where def = %s", n, def)
	}
}

// Reference: https://github.com/golang/protobuf/blob/c823c79ea1570fb5ff454033735a8e68575d1d0f/protoc-gen-go/descriptor/descriptor.proto#L136
func toType(field *descriptor.FieldDescriptorProto) string {
	label := field.GetLabel()
	res := ""
	switch *field.Type {
	case descriptor.FieldDescriptorProto_TYPE_INT32:
		res = "Int32"
	case descriptor.FieldDescriptorProto_TYPE_INT64:
		res = "Int64"
	case descriptor.FieldDescriptorProto_TYPE_SINT32:
		res = "Int32"
	case descriptor.FieldDescriptorProto_TYPE_SINT64:
		res = "Int64"
	case descriptor.FieldDescriptorProto_TYPE_SFIXED32:
		res = "Fixed Int32"
	case descriptor.FieldDescriptorProto_TYPE_SFIXED64:
		res = "Fixed Int64"
	case descriptor.FieldDescriptorProto_TYPE_UINT32:
		res = "Word32"
	case descriptor.FieldDescriptorProto_TYPE_UINT64:
		res = "Word64"
	case descriptor.FieldDescriptorProto_TYPE_FIXED32:
		res = "Fixed Word32"
	case descriptor.FieldDescriptorProto_TYPE_FIXED64:
		res = "Fixed Word64"
	case descriptor.FieldDescriptorProto_TYPE_STRING:
		res = "Text"
	case descriptor.FieldDescriptorProto_TYPE_BYTES:
		res = "ByteString"
	case descriptor.FieldDescriptorProto_TYPE_BOOL:
		res = "Bool"
	case descriptor.FieldDescriptorProto_TYPE_FLOAT:
		res = "Float"
	case descriptor.FieldDescriptorProto_TYPE_DOUBLE:
		res = "Double"
	case descriptor.FieldDescriptorProto_TYPE_MESSAGE:
		res = toHaskellType(field.GetTypeName())
	case descriptor.FieldDescriptorProto_TYPE_ENUM:
		res = toHaskellType(field.GetTypeName())
	default:
		Fail(fmt.Sprintf("no mapping for type %s", field.GetType()))
	}

	if label == descriptor.FieldDescriptorProto_LABEL_REPEATED {
		res = fmt.Sprintf("[%s]", res)
	} else if *field.Type == descriptor.FieldDescriptorProto_TYPE_MESSAGE {
		res = fmt.Sprintf("Maybe %s", res)
	}

	return res
}

// .foo.Message => Message
// google.protobuf.Empty => Google.Protobuf.Empty
func toHaskellType(s string) string {
	if len(s) > 1 && s[0:1] == "." {
		parts := strings.Split(s, ".")
		return parts[len(parts)-1]
	}

	parts := []string{}
	for _, x := range strings.Split(s, ".") {
		parts = append(parts, strings.Title(x))
	}
	return strings.Join(parts, ".")
}

// Enums to Haskell sum types
// ABOUT_FOO => AboutFoo
// SCREAMING_SNAKE_CASE to PascalCase.
func enumToHaskellSumType(s string) string {
	parts := []string{}
	for _, x := range strings.Split(s, "_") {
		parts = append(parts, strings.Title(strings.ToLower(x)))
	}
	return strings.Join(parts, "")
}

// snake_case to camelCase.
func toHaskellFieldName(s string) string {
	parts := []string{}
	for i, x := range strings.Split(s, "_") {
		if i == 0 {
			parts = append(parts, strings.ToLower(x))
		} else {
			parts = append(parts, strings.Title(strings.ToLower(x)))
		}
	}
	return strings.Join(parts, "")
}

// protoFilesToGenerate selects descriptor proto files that were explicitly listed on the command-line.
func (g *generator) protoFilesToGenerate() []*descriptor.FileDescriptorProto {
	files := []*descriptor.FileDescriptorProto{}
	for _, name := range g.genReq.FileToGenerate { // explicitly listed on the command-line
		for _, f := range g.genReq.ProtoFile { // all files and everything they import
			if f.GetName() == name { // match
				files = append(files, f)
				continue
			}
		}
	}
	return files
}

type indentation int

func (i indentation) String() string {
	return strings.Repeat("  ", int(i))
}

func print(buf *bytes.Buffer, tpl string, args ...interface{}) {
	buf.WriteString(fmt.Sprintf(tpl, args...))
	buf.WriteByte('\n')
}

func filePath(f *descriptor.FileDescriptorProto) string {
	return *f.Name
}

func onlyBase(path string) string {
	return filepath.Base(path)
}

func packageFileName(path string) string {
	ext := filepath.Ext(path)
	return strings.Title(strings.TrimSuffix(path, ext))
}

func toModuleName(pkgName string) string {
	parts := []string{}
	for _, p := range strings.Split(pkgName, ".") {
		parts = append(parts, strings.Title(p))
	}
	return strings.Join(parts, ".")
}

func Fail(msgs ...string) {
	s := strings.Join(msgs, " ")
	log.Print("error:", s)
	os.Exit(1)
}

func readGenRequest(r io.Reader) *plugin.CodeGeneratorRequest {
	data, err := ioutil.ReadAll(r)
	if err != nil {
		Fail(err.Error(), "reading input")
	}

	req := new(plugin.CodeGeneratorRequest)
	if err = proto.Unmarshal(data, req); err != nil {
		Fail(err.Error(), "parsing input proto")
	}

	if len(req.FileToGenerate) == 0 {
		Fail("no files to generate")
	}

	return req
}

func writeGenResponse(w io.Writer, resp *plugin.CodeGeneratorResponse) {
	data, err := proto.Marshal(resp)
	if err != nil {
		Fail(err.Error(), "marshaling response")
	}
	_, err = w.Write(data)
	if err != nil {
		Fail(err.Error(), "writing response")
	}
}
