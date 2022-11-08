import grpc
import greet_pb2
import greet_pb2_grpc
from concurrent import futures

class Greeter(greet_pb2_grpc.GreeterServicer):
    def SayHello(self,request,context):
        print(request.name)
        return greet_pb2.HelloReply(message="Hello! {}".format(request.name))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:8001')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()