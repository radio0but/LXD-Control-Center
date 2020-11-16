#!/bin/bash

cd /opt
git clone https://github.com/radio0but/LXD-Control-Center.git
cd ./LXD-Control-Center
random=$(tr -dc 'a-z0-9!@#$%^&*(-_=+)' < /dev/urandom | head -c50)
python3 -m venv venv
source venv/bin/activate
pip install psutil
pip install django
pip install requests
pip install django-lockdown
rm venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/base.html
rm venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/form.html
mv base.html venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/
mv form.html venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/
echo "SECRET_KEY = '$random'" >> ./LXDcontrolCENTER/settings.py
python manage.py migrate
python manage.py createsuperuser
