from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
# from celery.schedule import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Youtube_Channel.settings')

app = Celery('Youtube_Channel')
app.conf.enable_utc = False

app.conf.update(timezone="Asia/Kolkata")

app.config_from_object(settings, namespace="CELERY")

# Celery Beat Settings
app.conf.beat_schedule = {
    'every-15-seconds':{
        'task': 'celeryApp.tasks.send_mail',
        'schedule': 15,
        # 'schedule': crontab(='*/15')---> sonar(='*/15'),
        'args': ('billaanil3@gmail.com',)
    }
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.Request!r}")
