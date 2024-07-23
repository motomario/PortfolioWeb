from django.db import models
import uuid
from django.utils import timezone

class EmailTracking(models.Model):
    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField()
    opened = models.IntegerField(default=0)
    clicked = models.IntegerField(default=0)
    open_timestamp = models.DateTimeField(null=True, blank=True)
    click_timestamp = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email
