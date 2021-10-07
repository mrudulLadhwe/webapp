from django.http.response import Http404
from django.shortcuts import render
import base64
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import AppUsers
from .serializers import WebAppUserSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.validators import validate_email

# Create your views here.
class user(APIView):
    def post(self, request):
        data = request.data

        try:
            valid = validate_email(data["username"])
        except:
            return Response("Not Valid Email", status=status.HTTP_400_BAD_REQUEST)

        try:
            usr = AppUsers.objects.create(
                username=data["username"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["username"],
            )
            usr.set_password(data["password"])
            usr.save()
            serializer = WebAppUserSerializer(usr, many=False)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(
                "Either Duplicate username or username, password, firstname and lastname is missing",
                status=status.HTTP_400_BAD_REQUEST,
            )


class userSelf(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        auth = request.META["HTTP_AUTHORIZATION"].split()
        
        if len(auth) == 2:
            if auth[0].lower() == "basic":
                uname, passwd = base64.b64decode(auth[1]).decode("utf8").split(":", 1)
                usr = AppUsers.objects.get(username=uname)
                serializer = WebAppUserSerializer(usr, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("Error getting user", status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request):
        data = request.data
        # get user
        auth = request.META["HTTP_AUTHORIZATION"].split()
        if len(auth) == 2:
            if auth[0].lower() == "basic":
                uname, passwd = base64.b64decode(auth[1]).decode("utf8").split(":", 1)
                usr = AppUsers.objects.filter(username=uname).first()

        if (
            (data.get("username") != uname)
            or data.get("account_created")
            or data.get("account_updated")
        ):
            return Response(
                "Username,account_created or account_updated cannot be updated",
                status=status.HTTP_400_BAD_REQUEST,
            )

        # update user
        try:
            usr.first_name = data["first_name"]
            usr.last_name = data["last_name"]
            usr.set_password(data["password"])
            usr.save()
        except Exception as e:
            return Response(
                "All fields are mandatory", status=status.HTTP_404_NOT_FOUND
            )

        # serializer = WebAppUserSerializer(usr, many=False)
        return Response("User Updated", status=status.HTTP_204_NO_CONTENT)
