from django.db import models
import uuid

class EmailTracking(models.Model):
    email = models.EmailField()
    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    opened = models.IntegerField(default=0)
    clicked = models.IntegerField(default=0)
    open_timestamp = models.DateTimeField(null=True, blank=True)
    click_timestamp = models.DateTimeField(null=True, blank=True)

    # Adding the default manager explicitly
    objects = models.Manager()

    def __str__(self):
        return self.email
