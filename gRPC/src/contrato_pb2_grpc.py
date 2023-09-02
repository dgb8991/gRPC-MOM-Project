# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import contrato_pb2 as contrato__pb2


class FileListStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListFiles = channel.unary_unary(
                '/contrato.FileList/ListFiles',
                request_serializer=contrato__pb2.Empty.SerializeToString,
                response_deserializer=contrato__pb2.FileResponse.FromString,
                )


class FileListServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ListFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileListServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=contrato__pb2.Empty.FromString,
                    response_serializer=contrato__pb2.FileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'contrato.FileList', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileList(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ListFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/contrato.FileList/ListFiles',
            contrato__pb2.Empty.SerializeToString,
            contrato__pb2.FileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class FindFileStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.FindFiles = channel.unary_unary(
                '/contrato.FindFile/FindFiles',
                request_serializer=contrato__pb2.FileRequest.SerializeToString,
                response_deserializer=contrato__pb2.FileResponse.FromString,
                )


class FindFileServicer(object):
    """Missing associated documentation comment in .proto file."""

    def FindFiles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FindFileServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'FindFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.FindFiles,
                    request_deserializer=contrato__pb2.FileRequest.FromString,
                    response_serializer=contrato__pb2.FileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'contrato.FindFile', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FindFile(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def FindFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/contrato.FindFile/FindFiles',
            contrato__pb2.FileRequest.SerializeToString,
            contrato__pb2.FileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
