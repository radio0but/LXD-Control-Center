#!/bin/bash
####################################################################################
###                                                                              ###
###                Services Stopper  for LXD-Control-Center                      ###
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
## Make sure to be in the right folder for the apps pid files                     ##
cd /opt/LXD-Control-Center                                                        ##
## Kill LXDCC                                                                     ##
fuser -k 8082/tcp                                                                 ##
## Remove LXDCC pid file                                                          ##         
rm runserver_pid.txt                                                              ##
## Kill webssh                                                                    ##
fuser -k 8989/tcp                                                                 ##
## Remove webssh pid file                                                         ##
rm webssh_pid.txt                                                                 ##
##                                                                                ##
####################################################################################