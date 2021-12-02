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
sudo chmod 777 django.log
sudo python3 manage.py migrate
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/home/ubuntu/webapp/webApp/amazon-cloudwatch-agent.json -s
sudo nohup python3 manage.py runserver 0.0.0.0:8001 > /dev/null 2>&1 &
