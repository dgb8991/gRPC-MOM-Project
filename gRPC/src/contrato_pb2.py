# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contrato.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x63ontrato.proto\x12\x08\x63ontrato\"\x1c\n\x0b\x46ileRequest\x12\r\n\x05\x66iles\x18\x01 \x03(\t\"#\n\x0c\x46ileResponse\x12\x13\n\x0b\x66iles_found\x18\x01 \x03(\t\"\x07\n\x05\x45mpty2@\n\x08\x46ileList\x12\x34\n\tListFiles\x12\x0f.contrato.Empty\x1a\x16.contrato.FileResponse2F\n\x08\x46indFile\x12:\n\tFindFiles\x12\x15.contrato.FileRequest\x1a\x16.contrato.FileResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'contrato_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_FILEREQUEST']._serialized_start=28
  _globals['_FILEREQUEST']._serialized_end=56
  _globals['_FILERESPONSE']._serialized_start=58
  _globals['_FILERESPONSE']._serialized_end=93
  _globals['_EMPTY']._serialized_start=95
  _globals['_EMPTY']._serialized_end=102
  _globals['_FILELIST']._serialized_start=104
  _globals['_FILELIST']._serialized_end=168
  _globals['_FINDFILE']._serialized_start=170
  _globals['_FINDFILE']._serialized_end=240
# @@protoc_insertion_point(module_scope)