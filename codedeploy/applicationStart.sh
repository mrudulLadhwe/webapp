#!/bin/bash

cd /home/ubuntu/webapp/webApp
sudo python3 manage.py migrate
sudo python3 manage.py runserver 0.0.0.0:8001