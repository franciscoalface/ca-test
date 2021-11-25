from datetime import date, datetime
from uuid import uuid4

import factory
from django.db import models

from events.models import Error, Event


class EventFactory(factory.django.DjangoModelFactory):
    session_id = factory.LazyFunction(uuid4)
    category = factory.Sequence(lambda c: f"New category {c}")
    name = factory.Sequence(lambda n: f"New name {n}")
    data = {"key": "value"}
    timestamp = factory.LazyFunction(datetime.timestamp(datetime.now()))

    class Meta:
        model = Event


class ErrorFactory(factory.django.DjangoModelFactory):
    payload = "{'data': None}"
    message = "{'data': 'Payload data required.'}"

    class Meta:
        models = Error
