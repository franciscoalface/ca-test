import logging
import os

from celery import Celery

logger = logging.getLogger("Celery")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "the_eye.settings")

app = Celery("the_eye")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request}")
