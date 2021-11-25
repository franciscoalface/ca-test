import logging

from the_eye.celery import app as celery_app

from events.models import Error
from events.serializers import EventSerializer

logger = logging.getLogger("Celery")


@celery_app.task
def add_event(data: dict) -> None:
    try:
        serializer = EventSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    except Exception as ex:
        add_error.delay(str(data), str(ex))


@celery_app.task
def add_error(payload: str, error: str) -> None:
    Error.objects.create(payload=payload, message=error)
