#!/bin/bash
####################################################################################
###                                                                              ###
###                    Installer for LXD-Control-Center                          ###
###              LXD-Control-Center A simple web UI for LXD                      ###            
###                Copyright (C) 2020  Marc-André Legault                        ###              
###                                                                              ###   
###    This program is free software; you can redistribute it and/or modify      ###
###     it under the terms of the GNU General Public License as published by     ###
###     the Free Software Foundation; either version 2 of the License, or        ###
###                  (at your option) any later version.                         ###
###                                                                              ###
###        This program is distributed in the hope that it will be useful,       ###
###        but WITHOUT ANY WARRANTY; without even the implied warranty of        ###
###        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         ###
###              GNU General Public License for more details.                    ###
###                                                                              ###
###   You should have received a copy of the GNU General Public License along    ###
###   with this program; if not, write to the Free Software Foundation, Inc.,    ###
###        51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.           ###
###                                                                              ###
###                                                    Marc-André Legault        ###
###                                                    radio0but@gmail.com       ###
###                                                                              ###
###    LXD-Control-Center version 1, Copyright (C) 2020 Marc-André Legault       ### 
###         LXD-Control-Center comes with ABSOLUTELY NO WARRANTY;                ###
###      This is free software, and you are welcome to redistribute it           ###
###                       under certain conditions;                              ###
###                        For more detail go to:                                ###
###     https://github.com/radio0but/LXD-Control-Center/blob/main/LICENSE        ###
###                                                                              ###
###                                                                              ###
####################################################################################
##                                                                                ##
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
pip install requests
pip install webssh                                                              ##
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
##                                                                                ##
####################################################################################
