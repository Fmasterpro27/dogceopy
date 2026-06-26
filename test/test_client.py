from dogceopy.client import DogCEOClient


def test_client():
    client = DogCEOClient()

    assert client.base_url == "https://dog.ceo/api"

    client.close()


def test_context_manager():
    with DogCEOClient() as client:
        assert client.timeout == 30.0