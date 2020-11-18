#!/bin/bash
####################################################################################
###                                                                              ###
###                    Launcher for LXD-Control-Center                           ###
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
####################################################################################
##                                                                                ##
## Make sure to be in the right folder when executing manage.py                   ##
cd /opt/LXD-Control-Center                                                        ##
## Activate the python virtual environement                                       ##      
source venv/bin/activate                                                          ##  
## Start LXDCC on port 8082  0.0.0.0 means visible from any interface             ##
nohup python manage.py runserver 0.0.0.0:8082 > runserver.log 2>&1 &              ##
## Start Webssh on port 8989                                                      ##
nohup wssh --port=8989 > webssh.log 2>&1 &                                        ##
##                                                                                ##
####################################################################################  