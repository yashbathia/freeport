#!/usr/bin/env python
import argparse
import os
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument("portnumber", help="The number of the port you want free (Eg. 8000)",
                    type=int, default=None)

args = parser.parse_args()
port = args.portnumber

try:
    port = int(port)
    cmd = 'lsof -t -i:{0}'.format(port)
    pid = None
    try:
        pid = subprocess.check_output(cmd, shell=True)
    except Exception as e:
        print("No process running on port {} by current user. Checking if root is running the proecess".format(port))
        if pid is None:
            cmd = 'sudo lsof -t -i:{0}'.format(port)
            pid = subprocess.check_output(cmd, shell=True)
    pids =  pid.decode().split("\n")
    pids_int = []
    for pid in pids:
        if pid:
            pid = int(pid)
            pids_int.append(pid)
except ValueError as e:
    print(e)
    exit()
except Exception as e:
    print("No process found running on port {0}.".format(port))
    exit()

for pid in pids_int:
    processTypeCmd = 'ps -p {0} -o comm='.format(pid)
    processType = subprocess.check_output(processTypeCmd, shell=True, text=True).rstrip('\n')
    confirm = ''
    if processType:
        while True:
            try:
                confirm = raw_input("Process Type: '{0}'  Port: {1}. Kill?[yes/no]".format(processType, port))
            except NameError:
                confirm = input("Process Type: '{0}'  Port: {1}. Kill?[yes/no]".format(processType, port))

            confirm = confirm.lower()
            if confirm == 'yes' or confirm == 'no':
                break

    if confirm == 'yes':
        userCmd = 'ps -o user= -p {}'.format(pid)
        user = subprocess.check_output(userCmd, shell=True, text=True).rstrip('\n')
        if user.lower() == "root":
            killCmd = 'sudo kill -9 {0}'.format(pid)
        else:
            killCmd = 'kill -9 {0}'.format(pid)
        isKilled = os.system(killCmd)
        if isKilled == 0:
            print("Port {0} is free. Processs {1} killed successfully".format(port, pid))
        else:
            print("Cannot free port {0}.Failed to kill process {1}, err code:{2}".format(port, pid, isKilled))
    elif confirm == 'no':
        print("Skip killing process type {0} on port {1}".format(processType, port))
