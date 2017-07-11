# chat_server.py
# -*- coding: utf-8 -*-
from Process import *

import socket
import time
import os
#Contain Socket
SOCKET_LIST     = []
#Server Socket
server_socket   =None
#Get UserName
NickName        ={}

#[Object Socket] Send Hello To New USer
Tranf           =None

class Server:
    def __init__(self):
        os.system('clear')
        self.Ps             =Process()
        self.Host           = ''
        self.Port           =0
        self.msg            = Msg()
	self.c		    =bcolors()

    # Khoi Tao Server voi tham so mac dinh
    def BindServer(self,Port=4444,MaxClient=10):
        self.Port=Port
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.Host, Port))
        server_socket.listen(MaxClient)
	print bcolors.BOLD+bcolors.WARNING + "\n\nKhởi Tạo Server Thành công \n\n"+ 		bcolors.ENDC
        return server_socket


    # broadcast chat messages to all connected clients
    def broadcast(self,server_socket, sock, message):
        for socket in SOCKET_LIST:
            #send the message only to peer
            if socket != server_socket and socket != sock:
		#print "socket ",socket
                try:
                    socket.send(message)
                except:
                    # broken socket connection
                    socket.close()
                    # broken socket, remove it
                    if socket in SOCKET_LIST:
                        SOCKET_LIST.remove(socket)


    # Tao 1 Socket, [Ket noi den server de gui message to Client]
    def TranferToClient(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect((self.Host, self.Port))
        except:
            SOCKET_LIST.remove(socket)
        else:
            return s


    # Send messages to 1 connected client
    def SendtoClient(self,server_socket,Tranf,sock,message):
        for socket in SOCKET_LIST:
	    
            #send the message only to peer
            if socket != server_socket and socket != Tranf:
	        #print "socket ",socket
                try:
                    socket.send(message)
                except:
                    # broken socket connection
                    socket.close()
                    # broken socket, remove it
                    if socket in SOCKET_LIST:
                        SOCKET_LIST.remove(socket)

    # Thong bao den new user
    def MsgNewUser(self,sock, NewNickName):
        MessageContent=[]
        Message =bcolors.BOLD+bcolors.OKBLUE + "[ " + self.Ps.getCurrentDateTime('t') + " ]"+bcolors.ENDC+bcolors.OKGREEN+"- *****Chào mừng thành viên: "+NewNickName+" đã vào phòng chat"+bcolors.ENDC
        MessageContent.append(str(sock.getpeername()) + Message)
        MessageContent.append(Message)
        return MessageContent


    # Thong bao trung ten new user
    def MsgUserExist(self,sock, NewNickName):
        MessageContent=[]
        Message = "[ " + self.Ps.getCurrentDateTime('t') + " ]- #Tên : "+NewNickName+" đã tồn tại, vui lòng nhập tên khác"
        MessageContent.append(str(sock.getpeername()) + Message)
        MessageContent.append(Message)
        return MessageContent



    # Thong bao den user [Logout] huac mat ket noi
    def MsgUserLogout(self, sock):
        MessageContent = []
        Message = bcolors.BOLD+bcolors.OKBLUE+"[ " + self.Ps.getCurrentDateTime('t') + " ]"+bcolors.ENDC+bcolors.FAIL+"- ***** Thành viên: "+NickName[sock.getpeername()] + " Đã thoát!!!"+bcolors.ENDC
        MessageContent.append(NickName[sock.getpeername()] + Message)
        MessageContent.append(Message)
        return MessageContent

    # Hien Thi Message [Nhan duoc] tu user
    def ProcessRecvData(self,sock,RecvData):
        MessageContent = bcolors.BOLD+bcolors.OKBLUE+"[ " + self.Ps.getCurrentDateTime('t') + "]"+bcolors.ENDC+bcolors.White+"- "+ NickName[sock.getpeername()] + " - " + RecvData.strip().replace("\r\n","")
        #print "RecvData - MessageContent ",MessageContent
        return MessageContent

    # Xu li Recvdata chua thong so
    def ProcessData(self,server_socket,Tranf,sock,RecvData):
        #print "SOCKET_LIST ", SOCKET_LIST
        # Process User Login or Logout, And Broadcast to All User
        
        newSock         =sock
        newserverSocket =server_socket
        newTranf        =Tranf


        if "#user" in RecvData:
            # Anh xa Socket <-> User
            NewNickName = RecvData.split(":")[1].strip()
            for key,value in NickName.items():
                #print key,value
                if NewNickName in value:
                    NewNickName=value+str(1)
                    
            NickName[newSock.getpeername()] = NewNickName
                

            #print self.msg.msg2
            msgUsr=self.MsgNewUser(newSock, NewNickName)
            MessageContent = msgUsr[1]
            print msgUsr[0]
            #self.broadcast(newserverSocket, newSock, MessageContent)
            self.SendtoClient(newserverSocket, newTranf, newSock, MessageContent)
	    #self.server.broadcast(server_socket, sock, MessageContent)


                
        elif "#exit" in RecvData:
            try:
                msgUsrLogout = self.MsgUserLogout(newSock)
            except:
                pass

            else:
                # send data to Client
                MessageContent = msgUsrLogout[1]
                print msgUsrLogout[0]
                self.broadcast(newserverSocket, newSock, MessageContent)
                SOCKET_LIST.remove(newSock)


        #Recv Data And Broadcast to All User
        else:
            #print RecvData
            try:
                MessageContent = self.ProcessRecvData(newSock,RecvData)
                self.broadcast(newserverSocket, newSock, MessageContent)
                print MessageContent
            except:
                pass


