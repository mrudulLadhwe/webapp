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
    verified = serializers.BooleanField()
    verified_on = serializers.DateTimeField()

    class Meta:
        model = AppUsers


class UserProfilePic(serializers.Serializer):
    file_name = serializers.CharField()
    id = serializers.UUIDField(source="uuid")
    url = serializers.CharField()
    upload_date = serializers.DateField()
    user_id = serializers.UUIDField(source="uuid")

    class Meta:
        model = AppUsers


# fields = "__all__"
