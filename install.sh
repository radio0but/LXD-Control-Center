#!/bin/bash

# OS=$(awk '/DISTRIB_ID=/' /etc/*-release | sed 's/DISTRIB_ID=//' | tr '[:upper:]' '[:lower:]')
# ARCH=$(uname -m | sed 's/x86_//;s/i[3-6]86/32/')
# VERSION=$(awk '/DISTRIB_RELEASE=/' /etc/*-release | sed 's/DISTRIB_RELEASE=//' | sed 's/[.]0/./')

# if [ -z "$OS" ]; then
#     OS=$(awk '{print $1}' /etc/*-release | tr '[:upper:]' '[:lower:]')
# fi

# if [ -z "$VERSION" ]; then
#     VERSION=$(awk '{print $3}' /etc/*-release)
# fi

# if [ $OS == "ubuntu"]; then
#     apt install python3 git
# fi
# if [ $OS == "debian"]; then
#     apt install python3 git
# fi
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
rem venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/base.html
rem venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/form.html
mv base.html venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/
mv form.html venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/
echo "SECRET_KEY = '$random'" >> ./LXDcontrolCENTER/settings.py
python manage.py migrate
python manage.py createsuperuser
