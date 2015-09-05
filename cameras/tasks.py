from __future__ import absolute_import
from django.core import mail
from django.core.mail import EmailMessage
from django.conf import settings
from celery import shared_task

from os import path
import time

import picamera
   
def take_picture():
  timestr = time.strftime("%Y%m%d-%H%M%S") + ".jpg"
  store_to_path = path.join(settings.BASE_DIR, 'static/cameras/{filename}'.format(filename=timestr))
  with picamera.PiCamera() as camera:
    camera.capture(store_to_path)
  return store_to_path

@shared_task
def email_notification(name):
    email = EmailMessage('Hello', 'Something goes here', 'zhdhui@gmail.com',
              ['zhdhui@gmail.com'])
    
    email.attach_file(take_picture())
    email.send()      
    return email