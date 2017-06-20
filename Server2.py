# chat_server.py
#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import socket
import select
import time

HOST = '' 
SOCKET_LIST = []
RECV_BUFFER = 4096 
PORT = 4444
NickName={}
server_socket=''
data_Stream=""

#store to File
file_Store=open("file_Store.txt","wb")

#get CurrentDate or currentTime

def getCurrentDateTime(mode):
    try:
        if mode=='t':
            return time.strftime("%H:%M")
        elif mode=='d':
            return time.strftime("%d-%m-%Y")
    except:
        return ""
    
def showData(MessageContent,Mode):
    global data_Stream
    if Mode=='print':
        print MessageContent
    data_Stream+=MessageContent+"\n"
     
def Make_Server(HOST,PORT,MaxClient):
    #Make Server
    global server_socket
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(MaxClient)
    
def chat_server():
    #os.system('cls')
    global data_Stream
    print getCurrentDateTime('d')
    Make_Server(HOST, PORT,10)
    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)

    MessageContent="Chat server started on port " + str(PORT)
    showData(MessageContent,'print')
    
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
                    sock.send(welcome_Msg)
                    
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
                                        showData(data,'')
                                        print addr,"|user:",NickName[sock.getpeername()]
                                        welcome_Msg="\n-----------------Welcome to chatting room :"+usr
                                        broadcast(server_socket, sockfd,welcome_Msg)
                                        
                                elif "#exit" in data:
                                    try:
                                        SOCKET_LIST.remove(sock)
                                        MessageContent=str('-----------------'+NickName[sock.getpeername()])+' is offline'
                                        showData(MessageContent,'print')
                                        broadcast(server_socket, sock, MessageContent)
                                        continue
                                    except:
                                        pass

                            else:
                                    MessageContent=str('[' + getCurrentDateTime('t') + ']-' + NickName[sock.getpeername()] + '-' + data).strip()
                                    showData(MessageContent,'print')
                                    #send data to Client
                                    broadcast(server_socket, sock, MessageContent)
                                    
                                    # there is something in the socket
                        else:                            
                            # remove the socket that's broken    
                            if sock in SOCKET_LIST:
                                SOCKET_LIST.remove(sock)
                                # at this stage, no data means probably the connection has been broken
                            MessageContent=str(NickName[sock.getpeername()])+" is offline"
                            showData(MessageContent,'print')
                            broadcast(server_socket, sock, MessageContent)
                            #server command        
                            #sys.stdout.write('[Server] ');
                            #msg = sys.stdin.readline()
                            #broadcast(server_socket, sock, msg) 
                    # exception 
                    except:
                        MessageContent=str('-----------------'+NickName[sock.getpeername()])+' is offline'
                        showData(MessageContent,'print')
                        broadcast(server_socket, sock, MessageContent)
                        continue
    except:
        print "----------------------------------------------------------"
        print data_Stream
        file_Store.write(data_Stream)
        #server_socket.close()
        file_Store.close()

        
# broadcast chat messages to all connected clients
def broadcast(server_socket, sock, message):
    for socket in SOCKET_LIST:
        # send the message only to peer
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except:
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in SOCKET_LIST:
                    SOCKET_LIST.remove(socket)

               
if __name__ == "__main__":
    sys.exit(chat_server())   

