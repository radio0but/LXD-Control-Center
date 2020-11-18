# LXD Control Center

It is yet another simple UI for LXD with Django, Subprocess and webssh.
LXDCC allow you to manage your LXD containers all in a web interface. You can Start, Stop, Restart and delete container. For now you can launch Ubuntu20 CentOS6 and Arch(latest). Thanks to webssh its now possible to open containers in the terminal !

I do this project mainly to learn. 

Note that you need to have root acces and have LXD installed and initialized. You need a ssh server to use the webssh feature. All the command bellow have to be run as root user. Use the command : _sudo su_ to impersonate the root user if you are using sudo on your system.



![alt text](https://imgur.com/7zcIV74.png "Screenshot By the way lydianna is the hostame of the computer it was runnin on.")

### On many linux distro to install and initialize lxd


snap install lxd

lxd init

learn more on LXD with this good documentation !

https://linuxcontainers.org/lxd/getting-started-cli/

## To try LXD Control Center 

### install dependency :

#### Debian based OS :

_apt install python3 git wget_

#### Redhat based OS :

_yum install python3 git wget_

#### Arch based OS :

_pacman -S python3 git wget_

### download the install script :

_wget https://github.com/radio0but/LXD-Control-Center/releases/download/Version-1/install.sh_


Execute the install script to install LXD-Control-Center in your /opt folder:

### Make it excutable :

_chmod +x ./install.sh_

### And execute it

_./install.sh_

Its gonna ask for an username, an e-mail adress and a password

(You can leave the e-mail adress blank)

## To uninstall or Update

delete the folder /opt/LXD-Control-Center

_rm -r  /opt/LXD-Control-Center/_

then to update simply rerun the install script

## To start LXDCC:

First you have to make the *start.sh* script executable

*chmod +x /opt/LXD-Control-Center/start.sh*

Then run the start script

_/opt/LXD-Control-Center/start.sh_ 

The script will execute webssh and LXDCC in background

## To stop LXDCC:

First you have to make the *stop.sh* script executable

*chmod +x /opt/LXD-Control-Center/stop.sh*

Then run the stop script

_/opt/LXD-Control-Center/stop.sh_ 

## Almost Done

to see the UI go to http://localhost:8082/

Go to http://localhost:8082/admin to change your password and add users. Users need to have staff permission to access LXD-Control-Center

## Optional Settings

If you want the app to be visible on the network add your IP or 0.0.0.0 to /opt/LXD-Control-Center/settings.py 

_nano /opt/LXD-Control-Center/LXDcontrolCENTER/settings.py_

change
__ALLOWED_HOSTS = ["localhost"]__

To something like this

__ALLOWED_HOSTS = ["localhost","Yo.ur.Lo.cal.Ip","exemple.com"]__

Then you can use one of your containers as a reverse proxy. If you make webssh visible on the web make sure you have good passwords on your system... make sure you have good passwors period !  If you put webssh behind a reverse proxy change the variable wsshAdress in /opt/LXD-Control-Center/manage-containers/views.py __from__ _wsshAdress = "http://localhost:8989"_ __to__ wsshAdress = "https://ssh.yourdomain.com" 
 
