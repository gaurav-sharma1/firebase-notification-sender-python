import uuid
from django.db import models


class AppUser(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    username = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class FCMToken(models.Model):
    user = models.ForeignKey(
        AppUser,
        related_name='fcm_tokens',
        on_delete=models.CASCADE
    )
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token
from django.db import models

# Create your models here.
