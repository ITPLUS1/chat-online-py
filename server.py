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
    
    
    
if __name__=="__main__":
    Make_Server(HOST,PORT,10)
    while 1:
            conn, client = server.accept()
    try:
        print ("Connection from", client)
 
        while True:
            data = conn.recv(1024)
            print ("Receive from client:", data)
            if data:
                print ("Response to client")
                conn.sendall(data)
            else:
                print ("No data received")
                break
    finally:
        conn.close()
    
    
    
    
    
    
    
    
   
