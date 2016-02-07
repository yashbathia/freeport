# -*- coding: utf-8 -*-
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
    errMsg = 'Enter integer value for port number'
    port = int(port)
    cmd = 'lsof -t -i:{0}'.format(port)
    pid = subprocess.check_output(cmd, shell=True)
    pid = int(pid)
except ValueError:
    pid = None
    print(errMsg)
    exit()
except Exception as e:
    print("No process running on port {0}".format(port))
    exit()
killcmd = 'kill -9 {0}'.format(pid) if pid else None
isKilled = os.system('kill -9 {0}'.format(pid)) if pid else None
if isKilled == 0:
    print("Port {0} is free. Processs {1} killed successfully".format(port, pid))
else:
    print("Cannot free port {0}.Failed to kill process {1}, err code:{2}".format(port, pid, isKilled))

