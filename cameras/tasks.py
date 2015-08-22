from __future__ import absolute_import
from django.core import mail
from django.core.mail import EmailMessage
from django.conf import settings
from celery import shared_task

from os import path


@shared_task
def add(x, y):
  return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
    

@shared_task
def email_notification(name):
    email = EmailMessage('Hello', 'Something goes here', 'zhdhui@gmail.com',
              ['zhdhui@gmail.com'])
    email.attach_file(path.join(settings.BASE_DIR, 'static/cameras/1.jpg'))
    email.send()      
    return email