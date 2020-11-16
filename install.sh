#!/bin/bash
####################################################################################
###                                                                              ###
###                    Installer for LXD-Control-Center                          ###
###                                                                              ###
####################################################################################
####################################################################################
## change directory to /opt                                                       ##
cd /opt                                                                           ##
## Clone the files from github                                                    ##
git clone https://github.com/radio0but/LXD-Control-Center.git                     ##
## Change directory to LXD-Control-Center/                                        ##
cd ./LXD-Control-Center                                                           ##
## Create a random number for encryption                                          ##
random=$(tr -dc 'a-z0-9!@#$%^&*(-_=+)' < /dev/urandom | head -c50)                ##
## Create a Virtual environement for Python dependensies                          ##
python3 -m venv venv                                                              ##
## Enter in the virtual environement                                              ##
source venv/bin/activate                                                          ##
## Install Dependensies                                                           ##
pip install psutil                                                                ##
pip install django                                                                ##
pip install requests                                                              ##
pip install django-lockdown                                                       ##
## Remove the default templates for Django Lockdown                               ##
rm venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/base.html       ##
rm venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/form.html       ##
## Move the custom templates for Django Lockdown                                  ##  
mv base.html venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/      ##    
mv form.html venv/lib64/python3.8/site-packages/lockdown/templates/lockdown/      ##
## Add the random string to Lxd Control Center setting file                       ##
echo "SECRET_KEY = '$random'" >> ./LXDcontrolCENTER/settings.py                   ##
## create the sqlite database                                                     ##
python manage.py migrate                                                          ##
## Create root User for Lxd Control Center                                        ##            
python manage.py createsuperuser                                                  ##
####################################################################################
