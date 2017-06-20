# chat_server.py
#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import socket
import select
import time

sys.path.append("BLL")
from Server_Function import *

#HOST = ''
#SOCKET_LIST = []

RECV_BUFFER = 4096 
PORT = 4444
MaxClient=10
NickName={}
server_socket=''
data_Stream=""

#store to File
file_Store=open("file_Store.txt","wb")

#get CurrentDate or currentTime

def chat_server():
    server      =Server(PORT,MaxClient)
    process     =Process()
    #os.system('cls')
    print Server.getCurrentDateTime('d')

    #bind server
    #server.Make_Server(PORT,MaxClient)

    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)

    MessageContent="Chat server started on port " + str(PORT)
    process.show(MessageContent)
    
    try:
        while 1:
            # get the list sockets which are ready to be read through select
            # 4th arg, time_out  = 0 : poll and never block
            ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)
            #print ready_to_read,ready_to_write,in_error
            for sock in ready_to_read:        
                # a new connection request recieved
                if sock == server_socket:
                    sockfd, addr = server_socket.accept()
                    SOCKET_LIST.append(sockfd)

                    #sock.send(welcome_Msg)
                    
                    #broadcast(server_socket, sockfd,getCurrentDateTime('d'))
                    
                # a message from a client, not a new connection
                else:
                    # process data recieved from client, 
                    try:
                        # receiving data from the socket.
                        data = sock.recv(RECV_BUFFER)
                        if data:
                            #make NickName from client
                            if "#" in data:
                                if "#user" in data:
                                    try:
                                        usr=data.split(":")[1]
                                    except:
                                        pass
                                    else:
                                        NickName[addr]=usr
                                        process.show(data)

                                        print addr,"|user:",NickName[sock.getpeername()]

                                        server.SendtoClient(server_socket, sockfd,usr,'hello')
                                        
                                elif "#exit" in data:
                                    try:
                                        SOCKET_LIST.remove(sock)
                                        MessageContent=str('-----------------'+NickName[sock.getpeername()])+' is offline'
                                        process.show(MessageContent,)
                                        server.broadcast(server_socket, sock, MessageContent)
                                        continue
                                    except:
                                        pass

                            else:
                                    MessageContent=str('[' + getCurrentDateTime('t') + ']-' + NickName[sock.getpeername()] + '-' + data).strip()
                                    server.show(MessageContent)
                                    #send data to Client
                                    server.broadcast(server_socket, sock, MessageContent)
                                    
                                    # there is something in the socket
                        else:                            
                            # remove the socket that's broken    
                            if sock in SOCKET_LIST:
                                SOCKET_LIST.remove(sock)
                                # at this stage, no data means probably the connection has been broken
                            MessageContent=str(NickName[sock.getpeername()])+" is offline"
                            process.show(MessageContent)
                            server.broadcast(server_socket, sock, MessageContent)
                            #server command        
                            #sys.stdout.write('[Server] ');
                            #msg = sys.stdin.readline()
                            #broadcast(server_socket, sock, msg) 
                    # exception 
                    except:
                        MessageContent=str('-----------------'+NickName[sock.getpeername()])+' is offline'
                        process.show(MessageContent,'print')
                        server.broadcast(server_socket, sock, MessageContent)
                        continue
    except:
        print "----------------------------------------------------------"
        #print data_Stream
        #file_Store.write(data_Stream)
        #server_socket.close()
        #file_Store.close()

               
if __name__ == "__main__":
    sys.exit(chat_server())   

