from django.db import models

from events.managers import ErrorManager, EventManager


class Event(models.Model):
    session_id = models.UUIDField()
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    data = models.JSONField()
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = EventManager()

    class Meta:
        unique_together = [["session_id", "category", "name", "timestamp"]]


class Error(models.Model):
    payload = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ErrorManager()
