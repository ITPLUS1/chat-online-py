# chat_client.py
# -*- coding: utf-8 -*-

import os
import sys
import socket
import select
import time

from Client_BLL import *
from Process_DTL import *
socket_list=[]
class Client:
    def __init__(self):
        pr=Process()

    def ConnectServer(self,timeout):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
        except:
            return False
        else:
            return s

    # connect to remote host
    def TrytoConnect(self,s,host,port):
        try :
            s.connect((host, port))
        except :
            return False
        else:
            return True

    def StreamData(self,sock,s):
        if sock == s:
            # incoming message from remote server, s
            data = sock.recv(4096)
            if not data:
                print '\nNgắt kết nối từ Server!!!'
                sys.exit()

            else:
                sys.stdout.write(data + '\n>')
                sys.stdout.flush()
        else:
            # user entered a message
            sys.stdout.write('>')
            sys.stdout.flush()
            command = sys.stdin.readline()
            s.send(command)

            if '#exit' in command:
                print "GoodBye!!!"
                sys.exit()
