# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: generator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='generator.proto',
  package='generator',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fgenerator.proto\x12\tgenerator\"\x18\n\nGenRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"\x18\n\x08GenReply\x12\x0c\n\x04text\x18\x01 \x01(\t2E\n\tGenerator\x12\x38\n\x08generate\x12\x15.generator.GenRequest\x1a\x13.generator.GenReply\"\x00\x32\x41\n\x05Proxy\x12\x38\n\x08generate\x12\x15.generator.GenRequest\x1a\x13.generator.GenReply\"\x00\x62\x06proto3')
)




_GENREQUEST = _descriptor.Descriptor(
  name='GenRequest',
  full_name='generator.GenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='generator.GenRequest.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=30,
  serialized_end=54,
)


_GENREPLY = _descriptor.Descriptor(
  name='GenReply',
  full_name='generator.GenReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='generator.GenReply.text', index=0,
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
  serialized_start=56,
  serialized_end=80,
)

DESCRIPTOR.message_types_by_name['GenRequest'] = _GENREQUEST
DESCRIPTOR.message_types_by_name['GenReply'] = _GENREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenRequest = _reflection.GeneratedProtocolMessageType('GenRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENREQUEST,
  '__module__' : 'generator_pb2'
  # @@protoc_insertion_point(class_scope:generator.GenRequest)
  })
_sym_db.RegisterMessage(GenRequest)

GenReply = _reflection.GeneratedProtocolMessageType('GenReply', (_message.Message,), {
  'DESCRIPTOR' : _GENREPLY,
  '__module__' : 'generator_pb2'
  # @@protoc_insertion_point(class_scope:generator.GenReply)
  })
_sym_db.RegisterMessage(GenReply)



_GENERATOR = _descriptor.ServiceDescriptor(
  name='Generator',
  full_name='generator.Generator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=82,
  serialized_end=151,
  methods=[
  _descriptor.MethodDescriptor(
    name='generate',
    full_name='generator.Generator.generate',
    index=0,
    containing_service=None,
    input_type=_GENREQUEST,
    output_type=_GENREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GENERATOR)

DESCRIPTOR.services_by_name['Generator'] = _GENERATOR


_PROXY = _descriptor.ServiceDescriptor(
  name='Proxy',
  full_name='generator.Proxy',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=153,
  serialized_end=218,
  methods=[
  _descriptor.MethodDescriptor(
    name='generate',
    full_name='generator.Proxy.generate',
    index=0,
    containing_service=None,
    input_type=_GENREQUEST,
    output_type=_GENREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROXY)

DESCRIPTOR.services_by_name['Proxy'] = _PROXY

# @@protoc_insertion_point(module_scope)
