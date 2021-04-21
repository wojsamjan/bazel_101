"""The Python implementation of the GRPC fakeperson.FakePerson server."""

import fakeperson_pb2
import fakeperson_pb2_grpc
import grpc
import json
import logging
import requests
from concurrent import futures


class FakePerson(fakeperson_pb2_grpc.FakePersonServicer):
    def GetFakePersonData(self, request, context):
        print('Client: %s' % request.name)
        r = requests.get('https://api.namefake.com/english-united-states/male')
        json_data = json.loads(r.text)
        return fakeperson_pb2.FakePersonReply(name=json_data['name'], height=json_data['height'])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor())  # max_workers=10
    fakeperson_pb2_grpc.add_FakePersonServicer_to_server(FakePerson(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Listening on :50051')
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
