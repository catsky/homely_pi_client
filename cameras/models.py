import datetime

from django.db import models
from django.utils import timezone


class Image(models.Model):
  type = models.CharField(max_length=50)
  path = models.CharField(max_length=200)
  created_at = models.DateTimeField('date created')

  def was_created_recently(self):
    return self.created_at >= timezone.now() - datetime.timedelta(days=1)
  was_created_recently.admin_order_field = 'created_at'
  was_created_recently.boolean = True
  was_created_recently.short_description = 'Created recently?'
      
  def __str__(self):
    return self.path
      