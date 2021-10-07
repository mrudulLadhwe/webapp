import uuid
from django.db.models import fields
from rest_framework import serializers
from .models import AppUsers


class WebAppUserSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.EmailField()
    account_created = serializers.DateTimeField()
    account_updated = serializers.DateTimeField()

    class Meta:
        model = AppUsers


# fields = "__all__"
