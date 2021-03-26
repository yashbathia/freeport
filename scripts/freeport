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
errMsg = None

try:
    arr_of_pid = []
    errMsg = 'Enter integer value for port number'
    port = int(port)
    cmd = 'lsof -t -i:{0}'.format(port)
    pid = subprocess.check_output(cmd, shell=True)
    length_of_pid_str = len(pid)
    s = 0
    e = 0
    for x in pid:
        e += 1
        if x == '\n':
            arr_of_pid.append(pid[s:e-1])
            s = e
except ValueError:
    pid = None
    print(errMsg)
    exit()
except Exception as e:
    print("No process running on port {0}".format(port))
    exit()
for str_pid in arr_of_pid:
    pid = int(str_pid)
    processTypeCmd = 'ps -p {0} -o comm='.format(pid)
    processType = subprocess.check_output(processTypeCmd, shell=True).rstrip('\n')
    confirm = ''
    if processType:
        while True:
            confirm = raw_input("Process Type: '{0}'  Port: {1}. Kill?[yes/no]".format(processType, port))
            confirm = confirm.lower()
            if confirm == 'yes' or confirm == 'no':
                break

    if confirm == 'yes':

        killcmd = 'kill -9 {0}'.format(pid) if pid else None
        isKilled = os.system('kill -9 {0}'.format(pid)) if pid else None
        if isKilled == 0:
            print("Port {0} is free. Processs {1} killed successfully".format(port, pid))
        else:
            print("Cannot free port {0}.Failed to kill process {1}, err code:{2}".format(port, pid, isKilled))
