from django.shortcuts import render
import requests
import subprocess
import sys
import psutil
import socket
import datetime
import itertools
import base64
wsshAdress = "http://localhost:8989"
ttydAdress = "http://localhost:7681/" 

def convert(n): 
    return str(datetime.timedelta(seconds = n))

def button(request):
    #Get system Info
    ## Get Available Memory from psutil
    memoryAvailable = str(psutil.virtual_memory().available >> 30)
    ## Get Used Memory from psutil  
    memoryUsed = str(psutil.virtual_memory().used >> 30)
    ## Get Memory in percentage
    memoryPercent = str(psutil.virtual_memory().percent)
    ## CPU load in %
    cpuPercent = str(psutil.cpu_percent())
    ## Get HostName with Socket
    hostName = socket.gethostname()
    ## Get Uptime of the system from a bash script
    upTime = subprocess.run(["bash", "manageContainers/BASH/upTime.sh"],capture_output=True).stdout
    ### Remove the trash
    upTime = str(upTime).replace("\\n", "").replace("b", "").replace("'", "")
    # Get "lxc list -c n" output and converting it to a python list
    containers = subprocess.run(["lxc","list","-c","n"],capture_output=True).stdout
    containers = str(containers).replace("\\n", "").replace("-", "").replace("b\'", "")
    containers = containers.replace("\'", "").replace("+", "").replace("|", "").replace("+", "").replace("NAME", "").split()
    # Generates HTML code From the containers list
     ## Makes the <Input type=radio>
    htmlContainers = "<div class=\"item\"><input type=\"radio\" id=\"ContainerName\" name=\"ContainerName\" value=\"" 
    htmlContainers = htmlContainers + '\">:<div class=\"item\"><input type=\"radio\" name=\"ContainerName\" value=\"'.join(containers) + "\">"
    htmlContainers = htmlContainers.split(":")
    ## Makes the labels for the radio buttons
    htmlContainers1 = "<label for=\"ContainerName\">" + '</label><br></div>:<label for=\"ContainerName\">'.join(containers) + "</label><br></div>"
    htmlContainers1 = htmlContainers1.split(":")
    ## Alternate the two list's entries together in a new list
    htmlContainersFull = [x for x in itertools.chain.from_iterable(itertools.zip_longest(htmlContainers,htmlContainers1)) if x]
    ## Make a string from the new list
    htmlContainersFull = ''.join(htmlContainersFull)
    # Get Number of Containers from containers list
    numberContainers = len(containers)
    # Get the Date and time
    dateTime = datetime.datetime.now().strftime("%Y:%m:%d,%H:%M:%S")
    return render(request,'manageContainers/home.html',
    {
    'cpuPercent':cpuPercent,
    'memoryPercent':memoryPercent, 
    'memoryAvailable':memoryAvailable, 
    'memoryUsed':memoryUsed,
    'hostName': hostName,
    'upTime': upTime,
    'numberContainers' : numberContainers,
    'dateTime' : dateTime,
    'htmlContainersFull': htmlContainersFull,
    })
    



def output(request):
    #Get system Info
    ## Get Available Memory from psutil
    memoryAvailable = str(psutil.virtual_memory().available >> 30)
    ## Get Used Memory from psutil  
    memoryUsed = str(psutil.virtual_memory().used >> 30)
    ## Get Memory in percentage
    memoryPercent = str(psutil.virtual_memory().percent)
    ## CPU load in %
    cpuPercent = str(psutil.cpu_percent())
    ## Get HostName with Socket
    hostName = socket.gethostname()
    ## Get Uptime of the system from a bash script
    upTime = subprocess.run(["bash", "manageContainers/BASH/upTime.sh"],capture_output=True).stdout
    ### Remove the trash
    upTime = str(upTime).replace("\\n", "").replace("b", "").replace("'", "")
    # Get "lxc list -c n" output and converting it to a python list
    containers = subprocess.run(["lxc","list","-c","n"],capture_output=True).stdout
    containers = str(containers).replace("\\n", "").replace("-", "").replace("b\'", "")
    containers = containers.replace("\'", "").replace("+", "").replace("|", "")
    containers = containers.replace("+", "").replace("NAME", "").split()
    # Generates HTML code From the containers list
    ## Makes the <Input type=radio>
    htmlContainers = "<div class=\"item\"><input type=\"radio\" id=\"ContainerName\" name=\"ContainerName\" value=\""
    htmlContainers = htmlContainers + '\">:<div class=\"item\"><input type=\"radio\" name=\"ContainerName\" value=\"'.join(containers) + "\">"
    htmlContainers = htmlContainers.split(":")
    ## Makes the labels for the radio buttons
    htmlContainers1 = "<label for=\"ContainerName\">" + '</label><br></div>:<label for=\"ContainerName\">'.join(containers) + "</label><br></div>"
    htmlContainers1 = htmlContainers1.split(":")
    ## Alternate the two list's entries together in a new list
    htmlContainersFull = [x for x in itertools.chain.from_iterable(itertools.zip_longest(htmlContainers,htmlContainers1)) if x]
    ## Make a string from the new list
    htmlContainersFull = ''.join(htmlContainersFull)
    # Get Number of Containers from containers list
    numberContainers = len(containers)
    # Get the Date and time
    dateTime = datetime.datetime.now().strftime("%Y:%m:%d,%H:%M:%S")
    if request.POST:

 #### Get Input       
        containerName = request.POST.get('ContainerName')
        userName = request.POST.get('hostUserName')
        password = request.POST.get('hostUserPassword')
        if str(containerName) == "None":
            containerName = ""
        if str(userName) == "None":
            userName = ""
        if str(password) == "None":
            password = ""

 ##### Control Containers  

        if '_stop' in request.POST:
            if containerName != "":
                out= str(subprocess.run(["lxc", "stop", containerName], capture_output=True).stdout).replace("b''","")
                out = out + str(subprocess.run(["lxc", "stop", containerName], capture_output=True).stderr)
                out = out.replace("b''","").replace("b'","").replace("\\n'","")
                if out == "":
                    out = "<div class=\"footer\"><button class=\"accordion\"><h2>Success</h2></button><div class=\"panel\">"
                    out = out + "Succesfully stopped " + containerName + "</div></div>"
                else:
                    out = "<div class=\"footer\"><button class=\"accordion\"><h2>Something may be wrong</h2></button><div class=\"panel\">"
                    out = out + str(out) + "</div></div>"
            else:
                out= "Are you sure you want to stop a container <br> if youre sure you know what your doing select a container in the list and try again"
                out = "<div class=\"footer\"><button class=\"accordion\"><h2>Need Name</h2></button><div class=\"panel\">" + out + "</div></div>"
        elif '_start' in request.POST:
            if containerName != "":
                out= str(subprocess.run(["lxc", "start", containerName], capture_output=True).stdout).replace("b''","")
                out = out + str(subprocess.run(["lxc", "stop", containerName], capture_output=True).stderr)
                out = out.replace("b''","").replace("b'","").replace("\\n'","")
                if out != "":
                    out = "<div class=\"footer\"><button class=\"accordion\"><h2>Success</h2></button><div class=\"panel\">"
                    out = out + "Succesfully started " + containerName + "</div></div>"
                else:
                    out = "<div class=\"footer\"><button class=\"accordion\"><h2>Something may be wrong</h2></button><div class=\"panel\">" + str(out) + "</div></div>"
            else:
                out= "Want me to wake up a container ? <br> select a container in the list and try again"
                out = "<div class=\"footer\"><button class=\"accordion\"><h2>Need Name</h2></button><div class=\"panel\">" + str(out) + "</div></div>"
        elif '_restart' in request.POST:
            if containerName != "":
                out= str(subprocess.run(["lxc", "restart", containerName], capture_output=True).stdout).replace("b''","")
                out = out + str(subprocess.run(["lxc", "stop", containerName], capture_output=True).stderr).replace("b''","").replace("b'","").replace("\\n'","")
                if out != "":
                    out = "<div class=\"footer\"><button class=\"accordion\"><h2>Success</h2></button><div class=\"panel\">" + "Succesfully restarted " + containerName + "</div></div>"
                else:
                    out = "<div class=\"footer\"><button class=\"accordion\"><h2>Something may be wrong</h2></button><div class=\"panel\">" + str(out) + "</div></div>"
            else:
                out= "I see you are ready for a new start <br> select a container in the list if you want me to refresh something"
                out = "<div class=\"footer\"><button class=\"accordion\"><h2>Need Name</h2></button><div class=\"panel\">" + str(out) + "</div></div>"
        elif '_delete' in request.POST:
            if containerName != "":    
                out= str(subprocess.run(["lxc", "delete", containerName], capture_output=True).stdout).replace("b''","") 
                out = out + str(subprocess.run(["lxc", "stop", containerName], capture_output=True).stderr).replace("b''","").replace("b'","").replace("\\n'","")
                if out != "":
                    out = "<div class=\"footer\"><button class=\"accordion\"><h2>Success</h2></button><div class=\"panel\">" + "Succesfully deleted " + containerName + "</div></div>"
                else:
                    out = "<div class=\"footer\"><button class=\"accordion\"><h2>Something may be wrong</h2></button><div class=\"panel\">" + str(out) + "</div></div>"
            else:
                out= "Oh no, i dont know what to delete... <br> Maybe you want me to delete everything ? <br>...<br> Not a good idea i shall wait for you to select a container in the list and try again"
                out = "<div class=\"footer\"><button class=\"accordion\"><h2>Need Name</h2></button><div class=\"panel\">" + str(out) + "</div></div>"
        elif '_terminal' in request.POST:
            if containerName != "" and userName != "" and password != "":
                ## Webssh
                password_bytes = str(password).encode('ascii')
                base64_bytes = base64.b64encode(password_bytes)
                base64_password = base64_bytes.decode('ascii')
                str1 = "<div class=\"footer\"><button class=\"accordion\"><h2>" + containerName
                str2 = " Terminal</h2></button><div class=\"panel\">This will open the terminal in a new tab and execute bash on " + containerName
                str3 = " <a href=\"" + wsshAdress + "/?username=" + str(userName) + "&password=" + str(base64_password)
                str4 = "&hostname=localhost&command=sudo lxc exec " + containerName
                str5 = " bash\" target=\"_blank\"><h2>Open webssh</h2></a></div></div> <div id=\"terminal\"></div>" 
                out = str1 + str2 + str3 + str4 + str5
                ## ttyd
                # unampsswd = userName + ":" + password
                # subprocess.run([
                #     "nohup",  
                #     "manageContainers/BASH/ttyd_linux", 
                #     "-c" , 
                #     unampsswd  , 
                #     "lxc", 
                #     "exec" ,
                #     containerName, 
                #     "bash" , 
                #     ">", 
                #     "ttyd.log", 
                #     "2>&1", 
                #     "&&" , 
                #     "echo",
                #     "$1",
                #     ">",
                #     "ttyd_pid.txt" 
                #     ] )
                out = "<div class=\"footer\"><button class=\"accordion\"><h2>Need Name</h2></button><div class=\"panel\">  <iframe src+\"" + ttydAdress
                out = out + "\"> </iframe> <form action=\"output\" method=\"post\"> {% csrf_token %} <br><input class=\"button\" type=\"submit\" value=\"List Images\" name=\"_closeterminal\"> </form> </div><div id=\"terminal\"></div></div>"

            else:
                str1 = "Ok i ment opening the terminal inside a container ... <br> Here is a link to a simple ssh terminal   <br>...<br>"
                str2 = "use localhost as hostname and you local username and password to login<br> once your connected"
                str3 = " use the command \"sudo lxc exec nameofcontainer bash\"   <a href=\"" + wsshAdress
                str4 = "\"><h2>webssh link</h2></a> <br> Or select a container and clic the button "
                out= str1 + str2 +  str3 + str4
                out = "<div class=\"footer\"><button class=\"accordion\"><h2>Need Name</h2></button><div class=\"panel\">" + str(out) + "</div><div id=\"terminal\"></div></div>" 
        elif '_closeterminal' in request.POST:
                subprocess.run([
                    "kill",
                    "-9",
                    "'cat ttyd_pid.txt'",
                    "&&",
                    "rm",
                    "ttyd_pid.txt"
                ])


#### Launch Containers

        elif '_launchubuntu' in request.POST:
            if containerName != "":
                out= subprocess.run(["lxc","launch" , "ubuntu:x", containerName], capture_output=True)
                out = "<div class=\"footer\"><button class=\"accordion\"><h2>Success</h2></button><div class=\"panel\">" + str(out) + "</div></div>"
            else:
                out= "If your new to the the game you made a good choice by choosing ubuntu.<br> Please note that i need to give a name to the new container.<br> You can type it in the \"Container/VM Name\" text area"
                out = "<div class=\"footer\"><button class=\"accordion\"><h2>Need Name</h2></button><div class=\"panel\">" + str(out) + "</div></div>"
        elif '_launchcentos' in request.POST:
            if containerName != "":    
                out= subprocess.run(["lxc","launch" , "images:centos/7/amd64", containerName], capture_output=True) 
                out = "<div class=\"footer\"><button class=\"accordion\"><h2>Success</h2></button><div class=\"panel\">" + str(out) + "</div></div>" 
            else:
                out= "As a Pro IT you should know <br> Containers have Names !" 
                out = "<div class=\"footer\"><button class=\"accordion\"><h2>Need Name</h2></button><div class=\"panel\">" + str(out) + "</div></div>"         
        elif '_launcharch' in request.POST:
            if containerName != "":    
                out= subprocess.run(["lxc","launch" , "images:archlinux/current/amd64", containerName], capture_output=True)
                out = "<div class=\"footer\"><button class=\"accordion\"><h2>Success</h2></button><div class=\"panel\">" + str(out) + "</div></div>"  
            else:
                out= "By the way you use Arch...  <br> You Should Know I Need a Container Name !" 
                out = "<div class=\"footer\"><button class=\"accordion\"><h2>Need Name</h2></button><div class=\"panel\">" + str(out) + "</div></div>" 


        elif '_lxcImageList' in request.POST:
            
            out = str(subprocess.run(["lxc","image","list","--format","csv"], capture_output=True).stdout).replace("(release)","")
            out = out.replace(":","").replace("b\'","").replace(")",")").replace("'","").replace("\\n","").replace("no","<br>").replace("\"","").replace(","," ").split("(UTC)")
            out = "<div class=\"item\">" + '</div><div class=\"item\">'.join(out) + "</div>"
            out = "<div class=\"footer\"><button class=\"accordion\"><h2>Images list</h2></button><div class=\"panel\">" + out + "</div></div>"

            
        elif '_lxclist' in request.POST:   
            out = "<div class=\"item\">" +  str(subprocess.run(["lxc","list","--format","csv"], capture_output=True).stdout).replace(",0","</div><div class=\"item\">")
            out = out.replace("STOPPED","<div style=\"color: red;\" >STOPPED</div>").replace("RUNNING","<div style=\"color: green;\" >RUNNING</div>").replace("\\n","")
            out = out.replace(",","<br>").replace("<br><br>","<br>").replace("b\\","").replace("\'","")[1::] + "</div>"
            out = "<div class=\"footer\"><button class=\"accordion\"><h2>Containers List</h2></button><div class=\"panel\">" + out + "</div></div>"
        elif '_vmlist' in request.POST:
            out = "<div class=\"footer\"><button class=\"accordion\"><h2>Virtual Machines List</h2></button><div class=\"panel\"><iframe src=\"http://localhost:8989\"\></div></div>"
    print(out)

    return render(
        request,
        'manageContainers/home.html',{
            'data':out,
            'cpuPercent':cpuPercent,
            'memoryPercent':memoryPercent, 
            'memoryAvailable':memoryAvailable, 
            'memoryUsed':memoryUsed,
            'hostName': hostName,
            'upTime': upTime,
            'numberContainers' : numberContainers,
            'dateTime' : dateTime,
            'htmlContainersFull': htmlContainersFull,
            })

