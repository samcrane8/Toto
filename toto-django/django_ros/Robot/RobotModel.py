from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Robot(models.Model):
    name = models.TextField(null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    rosbridge_url = models.TextField(null=True)
