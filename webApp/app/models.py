from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AppUsers(AbstractUser):
    uuid = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        primary_key=True,
    )
    email = models.EmailField(max_length=254)
    username = models.EmailField(max_length=254, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    account_created = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, editable=False
    )
    account_updated = models.DateTimeField(
        auto_now=True, blank=True, null=True, editable=False
    )
    file_name = models.CharField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    upload_date = models.DateField(
        auto_now_add=True, blank=True, null=True, editable=False
    ) 
    verified = models.BooleanField(default=False, null=True, blank=True)
    verified_on = models.DateTimeField(
        blank=True, null=True, editable=False
    )

    REQUIRED_FIELDS = ["first_name", "last_name", "password", "file_name", "url"]

    class Meta:
        verbose_name = "Web App User"
        verbose_name_plural = "Web App Users"

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
