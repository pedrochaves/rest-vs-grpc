from app.grpc import calculator_pb2
from app.grpc import calculator_pb2_grpc


class CalculatorServer(calculator_pb2_grpc.CalculatorServicer):
    def _response(self, answer):
        return calculator_pb2_grpc.CalculatorResponse(answer=answer)

    def Add(self, request, context):
        return self._response(request.first_number + request.last_number)

    def Subtract(self, request, context):
        return self._response(request.first_number - request.last_number)

    def Multiply(self, request, context):
        return self._response(request.first_number * request.last_number)

    def Divide(self, request, context):
        return self._response(request.first_number / request.last_number)
