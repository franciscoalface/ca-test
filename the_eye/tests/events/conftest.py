import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture
def api_client(user):
    api_client = APIClient()
    return api_client.force_authenticate(user)


@pytest.fixture
def user():
    return User.objects.create(username="test_user", email="test_user@email.com")


@pytest.fixture(autouse=True)
def enable_db_access(db):
    pass


@pytest.fixture
def fake_payload():
    return {
        "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
        "category": "page interaction",
        "name": "pageview",
        "data": {"host": "www.consumeraffairs.com", "path": "/"},
        "timestamp": "2021-01-01 09:15:27.243860",
    }


@pytest.fixture
def fake_payload_list():
    return [
        {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "pageview",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/",
            },
            "timestamp": "2021-01-01 09:15:27.243860",
        },
        {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "page interaction",
            "name": "cta click",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/",
                "element": "chat bubble",
            },
            "timestamp": "2021-01-01 09:15:27.243860",
        },
        {
            "session_id": "e2085be5-9137-4e4e-80b5-f1ffddc25423",
            "category": "form interaction",
            "name": "submit",
            "data": {
                "host": "www.consumeraffairs.com",
                "path": "/",
                "form": {"first_name": "John", "last_name": "Doe"},
            },
            "timestamp": "2021-01-01 09:15:27.243860",
        },
    ]
