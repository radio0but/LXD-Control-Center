#!/bin/bash

apt install python3 git
git clone https://github.com/radio0but/LXD-Control-Center.git
random=$(tr -dc 'a-z0-9!@#$%^&*(-_=+)' < /dev/urandom | head -c50)
python3 -m venv venv
source venv/bin/activate
pip install psutil
pip install django
pip install requests
random="'"+ $random + "'"
awk -v secretKey="$random" '{print} /SECRET_KEY =/{print secretKey}' ./LXD-Control-Center/LXDcontrolCENTER/settings.py