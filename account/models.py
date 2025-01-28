from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _


class MessengerUser(AbstractUser):
    """
    Custom User model for the chat application.
    """
    # Additional fields
    avatar = models.ImageField(
        upload_to="avatars/",
        null=True,
        blank=True,
        help_text="Profile picture for the user"
    )
    is_online = models.BooleanField(
        default=False,
        help_text="Indicates whether the user is online"
    )
    last_seen = models.DateTimeField(
        null=True,
        blank=True,
        help_text="The last time the user was online"
    )

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def mark_online(self):
        """Mark the user as online."""
        self.is_online = True
        self.save()

    # def mark_offline(self):
    #     """Mark the user as offline and update last seen timestamp."""
    #     self.is_online = False
    #     self.last_seen = timezone.now()
    #     self.save()

    class Meta:
        verbose_name = _("messenger user")
        verbose_name_plural = _("messenger users")

