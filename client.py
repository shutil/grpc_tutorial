import grpc
import greet_pb2
import greet_pb2_grpc

channel = grpc.insecure_channel('localhost:8001')
stub = greet_pb2_grpc.GreeterStub(channel)
response = stub.SayHello(greet_pb2.HelloRequest(name="max"))
print(response)