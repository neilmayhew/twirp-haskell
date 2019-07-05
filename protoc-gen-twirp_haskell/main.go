// Generate Haskell Twirp Services based on the Servant web framework.
//
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
	"github.com/twitchtv/protogen/typemap"
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
	reg     *typemap.Registry
}

func (g *generator) Generate() *plugin.CodeGeneratorResponse {
	resp := new(plugin.CodeGeneratorResponse)

	for _, f := range g.protoFilesToGenerate() {
		twirpFileName := packageFileName(filePath(f)) + ".hs" // e.g. "hello_world/ServiceTwirp.hs"

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
	print(b, "-- Code generated by protoc-gen-twirp_haskell %s, DO NOT EDIT.", g.version)
	print(b, "{-# LANGUAGE TypeOperators #-}")

	pkgName := file.GetPackage()
	moduleName := toModuleName(file)

	print(b, "module %s where", moduleName)
	print(b, "")

	print(b, "import Servant")
	print(b, "import Twirp")
	print(b, "")
	print(b, "import %sPB", moduleName)
	print(b, "")

	comments, err := g.reg.FileComments(file)
	if err == nil && len(comments.LeadingDetached) > 0 {
		for _, cs := range comments.LeadingDetached {
			printComments(b, "", cs)
		}
		print(b, "")
	}

	services := []string{}
	for _, service := range file.Service {
		n := service.GetName()
		services = append(services, fmt.Sprintf("\"twirp\" :> \"%s.%s\" :> %sService", pkgName, n, n))
	}
	apis := strings.Join(services, "\n  :<|> ")
	apiName := packageType(filePath(file))

	print(b, "type %sAPI\n  =    %s", apiName, apis)

	for _, service := range file.Service {
		name := service.GetName()
		print(b, "")

		comments, err := g.reg.ServiceComments(file, service)
		if err == nil && comments.Leading != "" {
			printComments(b, "", comments.Leading)
		}

		print(b, "type %sService", name)

		for i, method := range service.GetMethod() {

			comments, err := g.reg.MethodComments(file, service, method)
			if err == nil && comments.Leading != "" {
				printComments(b, "  ", comments.Leading)
			}

			n := method.GetName()
			in := toHaskellType(method.GetInputType())
			out := toHaskellType(method.GetOutputType())
			sep := "  :<|>"
			if i == 0 {
				sep = "  =   "
			}
			print(b, "%s \"%s\" :> ReqBody [Protobuf, JSON] %s :> Post '[Protobuf, JSON] %s", sep, n, in, out)
		}

	}

	return b.String()
}

func printComments(b *bytes.Buffer, lead string, comments string) {
	text := strings.TrimSuffix(comments, "\n")
	for _, line := range strings.Split(text, "\n") {
		print(b, "%s-- %s", lead, line)
	}
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

func print(buf *bytes.Buffer, tpl string, args ...interface{}) {
	buf.WriteString(fmt.Sprintf(tpl, args...))
	buf.WriteByte('\n')
}

func filePath(f *descriptor.FileDescriptorProto) string {
	return *f.Name
}

func packageType(path string) string {
	ext := filepath.Ext(path)
	path = strings.TrimSuffix(filepath.Base(path), ext)
	return pascalCase(path)
}

func packageFileName(path string) string {
	ext := filepath.Ext(path)
	return pascalCase(strings.TrimSuffix(path, ext))
}

func toModuleName(file *descriptor.FileDescriptorProto) string {
	pkgName := file.GetPackage()

	parts := []string{}
	haskellPackage := getHaskellPackageOption(file)
	if haskellPackage != "" {
		parts = strings.Split(haskellPackage, ".")
	} else {
		for _, p := range strings.Split(pkgName, ".") {
			parts = append(parts, capitalize(p))
		}
	}

	apiName := packageType(filePath(file))
	parts = append(parts, apiName)

	return strings.Join(parts, ".")
}

func getHaskellPackageOption(file *descriptor.FileDescriptorProto) string {
	ex, _ := proto.GetExtension(file.Options, E_HaskellPackage)
	if ex != nil {
		asString := *ex.(*string)
		return asString
	}
	return ""
}

// capitalize, with exceptions for common abbreviations
func capitalize(s string) string {
	return strings.Title(strings.ToLower(s))
	// s = strings.ToLower(s)
	// switch s {
	// case "api":
	// 	return "API"
	// default:
	// 	return strings.Title(s)
	// }
}

// snake_case to PascalCase.
func pascalCase(s string) string {
	parts := []string{}
	for _, x := range strings.Split(s, "_") {
		parts = append(parts, capitalize(x))
	}
	return strings.Join(parts, "")
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
