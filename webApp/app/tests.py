from django.http import response
from django.test import TestCase, Client
from rest_framework.response import Response
import base64


class APITest(TestCase):
    def test_post_req(self):
        client = Client()
        paras = {
            "first_name": "Abhishek",
            "last_name": "Satbhai",
            "password": "Abhishek@1",
            "username": "shakee@gmail.com",
        }

        response = client.post("/v1/user", paras)
        assert response.status_code == 201

    def test_get_req(self):
        para = str(base64.b64encode(b"shakeee@gmail.com:Abhishek@1"), "utf-8")
        auth_headers = {
            "HTTP_AUTHORIZATION": "Basic " + para,
        }
        print(auth_headers["HTTP_AUTHORIZATION"])

        client = Client()
        response = client.get("/v1/user/self", **auth_headers)
        assert response.status_code == 401
