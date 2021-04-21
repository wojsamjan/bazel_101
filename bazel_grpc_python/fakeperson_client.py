"""The Python implementation of the GRPC fakeperson.FakePerson client."""

import fakeperson_pb2
import fakeperson_pb2_grpc
import grpc
import logging


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = fakeperson_pb2_grpc.FakePersonStub(channel)
        response = stub.GetFakePersonData(fakeperson_pb2.ClientNameRequest(name='Wojtek'))
    print('FakePerson: {name}, {height}cm'.format(name=response.name, height=response.height))


if __name__ == '__main__':
    logging.basicConfig()
    run()
