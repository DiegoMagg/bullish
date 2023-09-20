import os

from celery import Celery, Task
from django.conf import settings
from requests.exceptions import ConnectionError, ConnectTimeout, ReadTimeout

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bullish.settings')


class BaseTask(Task):
    autoretry_for = (ReadTimeout, ConnectionError, ConnectTimeout)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


app = Celery('bullish', task_cls=BaseTask)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.task_default_queue = settings.CELERY_QUEUE

app.conf.timezone = 'UTC'
