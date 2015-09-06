from __future__ import absolute_import

import os
from datetime import timedelta

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'homely_pi_client.settings')

from django.conf import settings

app = Celery('homely_pi_client')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')


app.conf.update(
  CELERYBEAT_SCHEDULE = {
      'add-every-120-seconds': {
          'task': 'cameras.tasks.email_notification',
          'schedule': timedelta(seconds=120),
          'args': ('catsky',)
      },
  },
  CELERY_TIMEZONE = 'Australia/Brisbane',
  CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
  BROKER_URL = 'django://'
)


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))