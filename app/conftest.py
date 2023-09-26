import pytest
from django.test import Client


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def authed_client(activated_user):
    client = Client()
    client.force_login(activated_user)
    return client
