from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from events.models import Error, Event
from events.serializers import ErrorSerializer, EventSerializer
from events.tasks import add_error, add_event


class EventAPIView(generics.ListCreateAPIView):
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        try:
            super().create(request, *args, **kwargs)
            return Response(status=status.HTTP_202_ACCEPTED)
        except ValidationError as error:
            add_error.delay(str(request.data), str(error))
            raise error

    def perform_create(self, serializer):
        add_event.delay(serializer.data)

    def get_queryset(self, queryset=None):
        return Event.objects.create_queryset(self.request.GET)


class ErrorAPIView(generics.ListAPIView):
    serializer_class = ErrorSerializer

    def get_queryset(self, queryset=None):
        return Error.objects.create_queryset(self.request.GET)
