from django.db import models


class EventManager(models.Manager):
    def create_queryset(self, params):
        queryset = self.get_queryset()
        queryset_filter = {}

        fields = ["session_id", "category"]
        for field in fields:
            if field in params and params.get(field, ""):
                queryset_filter[field] = params[field]

        start = params.get("start", None)
        end = params.get("end", None)
        if start and end:
            queryset_filter["timestamp__gte"] = start
            queryset_filter["timestamp__lte"] = end

        queryset = queryset.filter(**queryset_filter)
        return queryset


class ErrorManager(models.Manager):
    def create_queryset(self, params):
        queryset = self.get_queryset()
        queryset_filter = {}

        unexpected_value = params.get("unexpected_value", None)
        if unexpected_value:
            queryset_filter["message__icontains"] = unexpected_value

        timestamp = params.get("timestamp", None)
        if timestamp:
            queryset_filter["message__icontains"] = "Timestamp format not recognized"

        queryset = queryset.filter(**queryset_filter)
        return queryset
