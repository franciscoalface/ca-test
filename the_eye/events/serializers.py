from datetime import datetime, timedelta

from rest_framework import serializers

from events.models import Error, Event


class EventSerializer(serializers.ModelSerializer):
    def validate_data(self, value):
        if not value:
            raise serializers.ValidationError("Payload data required.")
        return value

    def validate_timestamp(self, value):
        value_timestamp = datetime.timestamp(value)
        timestamp_now = datetime.timestamp(datetime.now())
        if value_timestamp > timestamp_now:
            raise serializers.ValidationError("Future timestamp is not valid.")
        return value

    class Meta:
        model = Event
        fields = ["id", "session_id", "category", "name", "data", "timestamp"]


class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ["id", "payload", "message"]
