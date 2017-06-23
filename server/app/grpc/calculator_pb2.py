# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='calculator',
  syntax='proto3',
  serialized_pb=_b('\n\x10\x63\x61lculator.proto\x12\ncalculator\"=\n\x10\x43\x61lculateRequest\x12\x14\n\x0c\x66irst_number\x18\x01 \x01(\x02\x12\x13\n\x0blast_number\x18\x02 \x01(\x02\"#\n\x11\x43\x61lculateResponse\x12\x0e\n\x06\x61nswer\x18\x01 \x01(\x02\x32\xa9\x02\n\nCalculator\x12\x42\n\x03\x41\x64\x64\x12\x1c.calculator.CalculateRequest\x1a\x1d.calculator.CalculateResponse\x12G\n\x08Subtract\x12\x1c.calculator.CalculateRequest\x1a\x1d.calculator.CalculateResponse\x12G\n\x08Multiply\x12\x1c.calculator.CalculateRequest\x1a\x1d.calculator.CalculateResponse\x12\x45\n\x06\x44ivide\x12\x1c.calculator.CalculateRequest\x1a\x1d.calculator.CalculateResponseb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CALCULATEREQUEST = _descriptor.Descriptor(
  name='CalculateRequest',
  full_name='calculator.CalculateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_number', full_name='calculator.CalculateRequest.first_number', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_number', full_name='calculator.CalculateRequest.last_number', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=93,
)


_CALCULATERESPONSE = _descriptor.Descriptor(
  name='CalculateResponse',
  full_name='calculator.CalculateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='answer', full_name='calculator.CalculateResponse.answer', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['CalculateRequest'] = _CALCULATEREQUEST
DESCRIPTOR.message_types_by_name['CalculateResponse'] = _CALCULATERESPONSE

CalculateRequest = _reflection.GeneratedProtocolMessageType('CalculateRequest', (_message.Message,), dict(
  DESCRIPTOR = _CALCULATEREQUEST,
  __module__ = 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.CalculateRequest)
  ))
_sym_db.RegisterMessage(CalculateRequest)

CalculateResponse = _reflection.GeneratedProtocolMessageType('CalculateResponse', (_message.Message,), dict(
  DESCRIPTOR = _CALCULATERESPONSE,
  __module__ = 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:calculator.CalculateResponse)
  ))
_sym_db.RegisterMessage(CalculateResponse)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class CalculatorStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.Add = channel.unary_unary(
          '/calculator.Calculator/Add',
          request_serializer=CalculateRequest.SerializeToString,
          response_deserializer=CalculateResponse.FromString,
          )
      self.Subtract = channel.unary_unary(
          '/calculator.Calculator/Subtract',
          request_serializer=CalculateRequest.SerializeToString,
          response_deserializer=CalculateResponse.FromString,
          )
      self.Multiply = channel.unary_unary(
          '/calculator.Calculator/Multiply',
          request_serializer=CalculateRequest.SerializeToString,
          response_deserializer=CalculateResponse.FromString,
          )
      self.Divide = channel.unary_unary(
          '/calculator.Calculator/Divide',
          request_serializer=CalculateRequest.SerializeToString,
          response_deserializer=CalculateResponse.FromString,
          )


  class CalculatorServicer(object):

    def Add(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Subtract(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Multiply(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def Divide(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_CalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Add': grpc.unary_unary_rpc_method_handler(
            servicer.Add,
            request_deserializer=CalculateRequest.FromString,
            response_serializer=CalculateResponse.SerializeToString,
        ),
        'Subtract': grpc.unary_unary_rpc_method_handler(
            servicer.Subtract,
            request_deserializer=CalculateRequest.FromString,
            response_serializer=CalculateResponse.SerializeToString,
        ),
        'Multiply': grpc.unary_unary_rpc_method_handler(
            servicer.Multiply,
            request_deserializer=CalculateRequest.FromString,
            response_serializer=CalculateResponse.SerializeToString,
        ),
        'Divide': grpc.unary_unary_rpc_method_handler(
            servicer.Divide,
            request_deserializer=CalculateRequest.FromString,
            response_serializer=CalculateResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'calculator.Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaCalculatorServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Add(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Subtract(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Multiply(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def Divide(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaCalculatorStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def Add(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    Add.future = None
    def Subtract(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    Subtract.future = None
    def Multiply(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    Multiply.future = None
    def Divide(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    Divide.future = None


  def beta_create_Calculator_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('calculator.Calculator', 'Add'): CalculateRequest.FromString,
      ('calculator.Calculator', 'Divide'): CalculateRequest.FromString,
      ('calculator.Calculator', 'Multiply'): CalculateRequest.FromString,
      ('calculator.Calculator', 'Subtract'): CalculateRequest.FromString,
    }
    response_serializers = {
      ('calculator.Calculator', 'Add'): CalculateResponse.SerializeToString,
      ('calculator.Calculator', 'Divide'): CalculateResponse.SerializeToString,
      ('calculator.Calculator', 'Multiply'): CalculateResponse.SerializeToString,
      ('calculator.Calculator', 'Subtract'): CalculateResponse.SerializeToString,
    }
    method_implementations = {
      ('calculator.Calculator', 'Add'): face_utilities.unary_unary_inline(servicer.Add),
      ('calculator.Calculator', 'Divide'): face_utilities.unary_unary_inline(servicer.Divide),
      ('calculator.Calculator', 'Multiply'): face_utilities.unary_unary_inline(servicer.Multiply),
      ('calculator.Calculator', 'Subtract'): face_utilities.unary_unary_inline(servicer.Subtract),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_Calculator_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('calculator.Calculator', 'Add'): CalculateRequest.SerializeToString,
      ('calculator.Calculator', 'Divide'): CalculateRequest.SerializeToString,
      ('calculator.Calculator', 'Multiply'): CalculateRequest.SerializeToString,
      ('calculator.Calculator', 'Subtract'): CalculateRequest.SerializeToString,
    }
    response_deserializers = {
      ('calculator.Calculator', 'Add'): CalculateResponse.FromString,
      ('calculator.Calculator', 'Divide'): CalculateResponse.FromString,
      ('calculator.Calculator', 'Multiply'): CalculateResponse.FromString,
      ('calculator.Calculator', 'Subtract'): CalculateResponse.FromString,
    }
    cardinalities = {
      'Add': cardinality.Cardinality.UNARY_UNARY,
      'Divide': cardinality.Cardinality.UNARY_UNARY,
      'Multiply': cardinality.Cardinality.UNARY_UNARY,
      'Subtract': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'calculator.Calculator', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)