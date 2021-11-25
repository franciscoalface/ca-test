from unittest import mock

import pytest
from rest_framework.test import APIClient

from events.models import Event


@pytest.mark.parametrize(
    "url, expected", [("/api/events/", 401), ("/api/errors/", 401)]
)
def test_unauthenticated_request(url, expected):
    api_client = APIClient()
    response = api_client.get(url)
    assert expected == response.status_code


def test_create_event(api_client, fake_payload):
    url = "/api/events/"
    with mock.patch("events.views.add_error") as task:
        response = api_client.post(url, fake_payload, format="json")
        assert 202 == response.status_code
        assert 1 == Event.objects.all().count()
        assert not task.called
