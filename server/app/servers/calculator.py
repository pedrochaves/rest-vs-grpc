from app.grpc.calculator_pb2 import CalculatorServicer, CalculateResponse


class CalculatorServer(CalculatorServicer):

    def _response(self, answer):
        return CalculateResponse(answer=answer)

    def Add(self, request, context):
        return self._response(request.first_number + request.last_number)

    def Subtract(self, request, context):
        return self._response(request.first_number - request.last_number)

    def Multiply(self, request, context):
        return self._response(request.first_number * request.last_number)

    def Divide(self, request, context):
        return self._response(request.first_number / request.last_number)
