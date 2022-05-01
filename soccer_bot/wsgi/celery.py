import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

app = Celery("soccer_bot")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# setup celery_once
app.conf.ONCE = {
    "backend": "celery_once.backends.Redis",
    "settings": {
        "url": f"{settings.REDIS_ADDRESS}/{settings.REDIS_CACHE_DB}",
        "default_timeout": 60,
    },
}

app.conf.beat_schedule = {
    "delete_old_tokens": {
        "task": "api.tasks.cache_matches",
        "schedule": crontab(minute="*/10")
    },
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
