# chat_client.py
# -*- coding: utf-8 -*-
########################################
# Write by IT PLUS TEAM
########################################

import os
import sys
import socket
import select
import time

from Client_BLL import *
from Process_BLL import *
socket_list=[]
class Client:
    def __init__(self):
        pr=Process()

    # Khoi tao socket
    def ConnectServer(self,timeout):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
        except:
            return False
        else:
            return s

    # Ket noi den Server
    def TrytoConnect(self,s,host,port):
        try :
            s.connect((host, port))
        except :
            return False
        else:
            return True

    def StreamData(self,sock,s):
        if sock == s:
            # incoming message from remote server
            data = sock.recv(4096)
            if not data:
                print '\nNgắt kết nối từ Server!!!'
                sys.exit()

            else:
                # Hien thi du lieu
                sys.stdout.write(data + '\n>')
                #Xoa bo dem
                sys.stdout.flush()
        else:
            # user entered a message
            sys.stdout.write('>')
            # Xoa bo dem
            sys.stdout.flush()
            # Nhan du lieu tu keyboard
            command = sys.stdin.readline()
            # Gui du lieu
            s.send(command)

            if '#exit' in command:
                print "GoodBye!!!"
                sys.exit()
