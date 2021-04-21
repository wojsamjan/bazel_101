from fakeperson_server import FakePerson
from fakeperson_pb2 import ClientNameRequest


def test_fake_person_data_types():
    service = FakePerson()
    request = ClientNameRequest(name="Wojciech")

    response = service.GetFakePersonData(request, None)
    assert type(response.name) == str
    assert type(response.height) == int


if __name__ == '__main__':
    import pytest
    raise SystemExit(pytest.main([__file__]))
