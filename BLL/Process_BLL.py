#process
# -*- coding: utf-8 -*-
########################################
# Write by IT PLUS TEAM
########################################
import time
import socket
#get URL

import urllib

class Process:
    def __init__(self):
        pass

    def getCurrentDateTime(self, mode):
        try:
            if mode == 't':
                return time.strftime("%H:%M")
            elif mode == 'd':
                return time.strftime("%d-%m-%Y")
        except:
            return None

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'

    Purple='\033[0;35m'       # Purple
    Cyan='\033[0;36m'         # Cyan
    White='\033[0;97m'        # White
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



