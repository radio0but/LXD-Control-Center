#!/bin/bash

apt install python3 git
cd /opt
git clone https://github.com/radio0but/LXD-Control-Center.git
cd ./LXD-Control-Center
random=$(tr -dc 'a-z0-9!@#$%^&*(-_=+)' < /dev/urandom | head -c50)
python3 -m venv venv
source venv/bin/activate
mv base.html venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/
mv form.html venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/
pip install psutil
pip install django
pip install requests
pip install django-lockdown
echo "SECRET_KEY = '$random'" >> ./LXDcontrolCENTER/settings.py