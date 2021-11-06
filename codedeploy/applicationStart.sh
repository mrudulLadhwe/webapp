#!/bin/bash

cd /home/ubuntu/webapp/webApp
sudo apt install -y python3-pip
sudo pip install -r requirement.txt
sudo apt-get install -y python3-psycopg2
ls
sudo python3 manage.py migrate
sudo python3 manage.py runserver 0.0.0.0:8001