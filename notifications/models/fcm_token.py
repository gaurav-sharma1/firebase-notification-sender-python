from django.db import models

from .app_user import AppUser


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