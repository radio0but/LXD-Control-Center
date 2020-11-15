# LXD Control Center

It is yet another simple UI for LXD with Django and Subprocess.
Easily manage your Linux containers from any devices. Note that you need to have LXD installed and initialized. 

![alt text](https://imgur.com/7zcIV74.png "Screenshot")
By the way lydianna is the hostame of the computer it was runnin on.
### on many linux distro to install and initialize lxd

snap install lxd

lxd init

## To try LXD Control Center 

Note that for now the script only work on Debian based os using aptitude. Will be fixed soon though for now you can modify the script to fit your package manager.

simply execute the install script to install LXD-Control-Center in your /opt folder:

make it excutable :

chmod +x ./install.sh

And execute it

./install.sh



## Then to start the server:

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
