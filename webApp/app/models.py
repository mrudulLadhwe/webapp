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

    REQUIRED_FIELDS = ["first_name", "last_name", "password"]

    class Meta:
        verbose_name = "Web App User"
        verbose_name_plural = "Web App Users"

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


# class WebAppUsers(models.Model):
#     uuid = models.UUIDField(
#         unique=True, default=uuid.uuid4, editable=False, primary_key=True
#     )
#     email = models.EmailField(max_length=254)
#     username = models.EmailField(max_length=254, unique=True, blank=True, null=True)
#     password = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     account_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
#     account_updated = models.DateTimeField(auto_now=True, blank=True, null=True)

#     class Meta:
#         verbose_name = "Web App User"
#         verbose_name_plural = "Web App Users"

#     def __str__(self) -> str:
#         return self.first_name + " " + self.last_name
