# chat_server.py
import os
import sys
import socket
import time

HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 4444
NickName={}
server_socket=''
data_Stream=""

def Make_Server(HOST,PORT,MaxClient):
    #Make Server
    global server_socket
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(MaxClient)
    
   
