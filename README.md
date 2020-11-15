# LXD Control Center

It is yet another simple UI for LXD with Django and Subprocess.
Easily manage your Linux containers from any devices. Note that you need to have root acces and have LXD installed and initialized. All the command bellow have to be run as root user. sudo wont suffice in this case



![alt text](https://imgur.com/7zcIV74.png "Screenshot By the way lydianna is the hostame of the computer it was runnin on.")

### on many linux distro to install and initialize lxd

use the command : _sudo su_ to impersonate the root user

snap install lxd

lxd init

learn more on LXD

https://linuxcontainers.org/lxd/getting-started-cli/

## To try LXD Control Center 

Note that for now the script only work on Debian based os using aptitude. Will be fixed soon though for now you can modify the script to fit your package manager. i only use the package manager to instal git and Python3. The rest of the dependency get installed in a python virtual environement(venv). 

Execute the install script to install LXD-Control-Center in your /opt folder:

Make it excutable :

chmod +x ./install.sh

And execute it

./install.sh

## To uninstall or Update

delete the folder /opt/LXD-Control-Center

then to update simply rerun the install script

## To start the server:

First you have to make the *start.sh* script executable

*chmod +x /opt/LXD-Control-Center/start.sh*

Then run the start script

/opt/LXD-Control-Center/start.sh 

## Almost Done

to see the UI go to http://localhost:8383/

Go to http://localhost:8383/admin to change your password 

Default user name:

admin

Default Password:

lxccontrolcenter
