import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Image


class ImageMethodTests(TestCase):

    def test_was_created_recently_with_future_image(self):
        """
        was_created_recently() should return False for questions whose
        created_at is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_image = Image(created_at=time)
        self.assertEqual(future_image.was_created_recently(), False)
