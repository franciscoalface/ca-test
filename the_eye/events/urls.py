from django.urls import include, path

from events.views import ErrorAPIView, EventAPIView

urlpatterns = [
    path("events/", EventAPIView.as_view()),
    path("errors/", ErrorAPIView.as_view()),
]
