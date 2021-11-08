#!/bin/bash

cd /home/ubuntu
ls
cd webapp
ls
sudo apt install -y python3-pip
cd webApp
sudo pip install -r requirement.txt
sudo apt-get install -y python3-psycopg2
pip freeze
ls
sudo python3 manage.py migrate
sudo screen -d -m python manage.py runserver 0.0.0.0:8001