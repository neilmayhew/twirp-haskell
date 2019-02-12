# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: haberdasher.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='haberdasher.proto',
  package='twirp.example.haberdasher',
  syntax='proto3',
  serialized_options=_b('Z\013haberdasher'),
  serialized_pb=_b('\n\x11haberdasher.proto\x12\x19twirp.example.haberdasher\"\x16\n\x04Size\x12\x0e\n\x06inches\x18\x01 \x01(\x05\"2\n\x03Hat\x12\x0e\n\x06inches\x18\x01 \x01(\x05\x12\r\n\x05\x63olor\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\"\xcf\x01\n\x04\x42ill\x12/\n\x05price\x18\x01 \x01(\x0b\x32 .twirp.example.haberdasher.Price\x12=\n\x06status\x18\x02 \x01(\x0e\x32-.twirp.example.haberdasher.Bill.BillingStatus\x12\x12\n\x08vat_info\x18\x03 \x01(\tH\x00\x12\x12\n\x08zip_code\x18\x04 \x01(\tH\x00\"&\n\rBillingStatus\x12\x0b\n\x07UN_PAID\x10\x00\x12\x08\n\x04PAID\x10\x01\x42\x07\n\x05\x65xtra\"K\n\x04Test\x12\r\n\x05items\x18\x01 \x03(\x05\x12\x34\n\nalt_prices\x18\x02 \x03(\x0b\x32 .twirp.example.haberdasher.Price\"\'\n\x05Price\x12\x0f\n\x07\x64ollars\x18\x01 \x01(\r\x12\r\n\x05\x63\x65nts\x18\x02 \x01(\r\"\x17\n\x04Ping\x12\x0f\n\x07service\x18\x01 \x01(\t\"i\n\x04Pong\x12\x0e\n\x06status\x18\x01 \x01(\t\x12.\n\x05stuff\x18\x02 \x03(\x0b\x32\x1f.twirp.example.haberdasher.Test\x12\x0b\n\x01t\x18\x03 \x01(\rH\x00\x12\x0b\n\x01u\x18\x04 \x01(\tH\x00\x42\x07\n\x05\x65xtra2\xa5\x01\n\x0bHaberdasher\x12J\n\x07MakeHat\x12\x1f.twirp.example.haberdasher.Size\x1a\x1e.twirp.example.haberdasher.Hat\x12J\n\x07GetBill\x12\x1e.twirp.example.haberdasher.Hat\x1a\x1f.twirp.example.haberdasher.Bill2S\n\x06Health\x12I\n\x05\x43heck\x12\x1f.twirp.example.haberdasher.Ping\x1a\x1f.twirp.example.haberdasher.PongB\rZ\x0bhaberdasherb\x06proto3')
)



_BILL_BILLINGSTATUS = _descriptor.EnumDescriptor(
  name='BillingStatus',
  full_name='twirp.example.haberdasher.Bill.BillingStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UN_PAID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAID', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=285,
  serialized_end=323,
)
_sym_db.RegisterEnumDescriptor(_BILL_BILLINGSTATUS)


_SIZE = _descriptor.Descriptor(
  name='Size',
  full_name='twirp.example.haberdasher.Size',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inches', full_name='twirp.example.haberdasher.Size.inches', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=48,
  serialized_end=70,
)


_HAT = _descriptor.Descriptor(
  name='Hat',
  full_name='twirp.example.haberdasher.Hat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inches', full_name='twirp.example.haberdasher.Hat.inches', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='twirp.example.haberdasher.Hat.color', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='twirp.example.haberdasher.Hat.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=122,
)


_BILL = _descriptor.Descriptor(
  name='Bill',
  full_name='twirp.example.haberdasher.Bill',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='twirp.example.haberdasher.Bill.price', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='twirp.example.haberdasher.Bill.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vat_info', full_name='twirp.example.haberdasher.Bill.vat_info', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zip_code', full_name='twirp.example.haberdasher.Bill.zip_code', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BILL_BILLINGSTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='extra', full_name='twirp.example.haberdasher.Bill.extra',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=125,
  serialized_end=332,
)


_TEST = _descriptor.Descriptor(
  name='Test',
  full_name='twirp.example.haberdasher.Test',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='twirp.example.haberdasher.Test.items', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alt_prices', full_name='twirp.example.haberdasher.Test.alt_prices', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=409,
)


_PRICE = _descriptor.Descriptor(
  name='Price',
  full_name='twirp.example.haberdasher.Price',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dollars', full_name='twirp.example.haberdasher.Price.dollars', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cents', full_name='twirp.example.haberdasher.Price.cents', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=450,
)


_PING = _descriptor.Descriptor(
  name='Ping',
  full_name='twirp.example.haberdasher.Ping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='twirp.example.haberdasher.Ping.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=452,
  serialized_end=475,
)


_PONG = _descriptor.Descriptor(
  name='Pong',
  full_name='twirp.example.haberdasher.Pong',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='twirp.example.haberdasher.Pong.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stuff', full_name='twirp.example.haberdasher.Pong.stuff', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='t', full_name='twirp.example.haberdasher.Pong.t', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='u', full_name='twirp.example.haberdasher.Pong.u', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='extra', full_name='twirp.example.haberdasher.Pong.extra',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=477,
  serialized_end=582,
)

_BILL.fields_by_name['price'].message_type = _PRICE
_BILL.fields_by_name['status'].enum_type = _BILL_BILLINGSTATUS
_BILL_BILLINGSTATUS.containing_type = _BILL
_BILL.oneofs_by_name['extra'].fields.append(
  _BILL.fields_by_name['vat_info'])
_BILL.fields_by_name['vat_info'].containing_oneof = _BILL.oneofs_by_name['extra']
_BILL.oneofs_by_name['extra'].fields.append(
  _BILL.fields_by_name['zip_code'])
_BILL.fields_by_name['zip_code'].containing_oneof = _BILL.oneofs_by_name['extra']
_TEST.fields_by_name['alt_prices'].message_type = _PRICE
_PONG.fields_by_name['stuff'].message_type = _TEST
_PONG.oneofs_by_name['extra'].fields.append(
  _PONG.fields_by_name['t'])
_PONG.fields_by_name['t'].containing_oneof = _PONG.oneofs_by_name['extra']
_PONG.oneofs_by_name['extra'].fields.append(
  _PONG.fields_by_name['u'])
_PONG.fields_by_name['u'].containing_oneof = _PONG.oneofs_by_name['extra']
DESCRIPTOR.message_types_by_name['Size'] = _SIZE
DESCRIPTOR.message_types_by_name['Hat'] = _HAT
DESCRIPTOR.message_types_by_name['Bill'] = _BILL
DESCRIPTOR.message_types_by_name['Test'] = _TEST
DESCRIPTOR.message_types_by_name['Price'] = _PRICE
DESCRIPTOR.message_types_by_name['Ping'] = _PING
DESCRIPTOR.message_types_by_name['Pong'] = _PONG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Size = _reflection.GeneratedProtocolMessageType('Size', (_message.Message,), dict(
  DESCRIPTOR = _SIZE,
  __module__ = 'haberdasher_pb2'
  # @@protoc_insertion_point(class_scope:twirp.example.haberdasher.Size)
  ))
_sym_db.RegisterMessage(Size)

Hat = _reflection.GeneratedProtocolMessageType('Hat', (_message.Message,), dict(
  DESCRIPTOR = _HAT,
  __module__ = 'haberdasher_pb2'
  # @@protoc_insertion_point(class_scope:twirp.example.haberdasher.Hat)
  ))
_sym_db.RegisterMessage(Hat)

Bill = _reflection.GeneratedProtocolMessageType('Bill', (_message.Message,), dict(
  DESCRIPTOR = _BILL,
  __module__ = 'haberdasher_pb2'
  # @@protoc_insertion_point(class_scope:twirp.example.haberdasher.Bill)
  ))
_sym_db.RegisterMessage(Bill)

Test = _reflection.GeneratedProtocolMessageType('Test', (_message.Message,), dict(
  DESCRIPTOR = _TEST,
  __module__ = 'haberdasher_pb2'
  # @@protoc_insertion_point(class_scope:twirp.example.haberdasher.Test)
  ))
_sym_db.RegisterMessage(Test)

Price = _reflection.GeneratedProtocolMessageType('Price', (_message.Message,), dict(
  DESCRIPTOR = _PRICE,
  __module__ = 'haberdasher_pb2'
  # @@protoc_insertion_point(class_scope:twirp.example.haberdasher.Price)
  ))
_sym_db.RegisterMessage(Price)

Ping = _reflection.GeneratedProtocolMessageType('Ping', (_message.Message,), dict(
  DESCRIPTOR = _PING,
  __module__ = 'haberdasher_pb2'
  # @@protoc_insertion_point(class_scope:twirp.example.haberdasher.Ping)
  ))
_sym_db.RegisterMessage(Ping)

Pong = _reflection.GeneratedProtocolMessageType('Pong', (_message.Message,), dict(
  DESCRIPTOR = _PONG,
  __module__ = 'haberdasher_pb2'
  # @@protoc_insertion_point(class_scope:twirp.example.haberdasher.Pong)
  ))
_sym_db.RegisterMessage(Pong)


DESCRIPTOR._options = None

_HABERDASHER = _descriptor.ServiceDescriptor(
  name='Haberdasher',
  full_name='twirp.example.haberdasher.Haberdasher',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=585,
  serialized_end=750,
  methods=[
  _descriptor.MethodDescriptor(
    name='MakeHat',
    full_name='twirp.example.haberdasher.Haberdasher.MakeHat',
    index=0,
    containing_service=None,
    input_type=_SIZE,
    output_type=_HAT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBill',
    full_name='twirp.example.haberdasher.Haberdasher.GetBill',
    index=1,
    containing_service=None,
    input_type=_HAT,
    output_type=_BILL,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HABERDASHER)

DESCRIPTOR.services_by_name['Haberdasher'] = _HABERDASHER


_HEALTH = _descriptor.ServiceDescriptor(
  name='Health',
  full_name='twirp.example.haberdasher.Health',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=752,
  serialized_end=835,
  methods=[
  _descriptor.MethodDescriptor(
    name='Check',
    full_name='twirp.example.haberdasher.Health.Check',
    index=0,
    containing_service=None,
    input_type=_PING,
    output_type=_PONG,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HEALTH)

DESCRIPTOR.services_by_name['Health'] = _HEALTH

# @@protoc_insertion_point(module_scope)
