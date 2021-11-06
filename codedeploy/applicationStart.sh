#!/bin/bash

cd /home/ubuntu/webapp/webApp
ls
sudo apt install -y python3-pip
sudo pip install -r requirement.txt
pip freeze
ls
sudo python3 manage.py migrate
sudo python3 manage.py runserver 0.0.0.0:8001