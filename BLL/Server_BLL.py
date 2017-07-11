# chat_server.py
# -*- coding: utf-8 -*-
# Chuong trinh chat online
# Nguyen Dinh Thai - thai.itplus@gmail.com - fb: chickns0up
#
#
#
#
#
#

##########################################################################

from Process_BLL import *

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


##########################################################################


class Server:
    def __init__(self):
        os.system('clear')
        self.Ps             =Process()
        self.Host           = ''
        self.msg            = Msg()
	self.c		    =bcolors()
	self.Server	    ="1"
	self.Port1=self.Port2=None


    #Bind Server
    def Bind(self,Port,MaxClient):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.Host, Port))
        server_socket.listen(MaxClient)
        return server_socket
    

    # Khoi Tao Server voi tham so mac dinh
    def BindServer(self,Port=4444,Port2=4445,MaxClient=10):

        self.Port1  =Port
        self.Port2  =Port2
        
        try:
            # [thong bao] Khoi tao [server 1]
            self.Ps.msgServerBind(Port)
            
            # [Khoi tao server 1]
            server_socket=self.Bind(Port,MaxClient)
            
        except:
        #----------------------------------------------------
            try:
                # [thong bao] Server 1 ban, huac bi loi
                self.Ps.msgServerBusy(Port2)                

                # [thong bao] Khoi tao [server 2]
                self.Ps.msgServerBind(Port2)
                
                # [Khoi tao server 2]
                server_socket=self.Bind(Port2,MaxClient)

            except:
                # [thong bao]  =Loi khi tao server
                self.Ps.msgServerError(Port2)
                return None
                
            else:
                # [thong bao] khoi tao thanh cong
                self.Ps.ServerMsg("on")
                
                # [thong bao] Lay dia chi IP
                self.Ps.msgServerOnline()

                # [thong bao] Server da san sang
                self.Ps.Line()
                
                # Server Name
                self.Server="2"

                return server_socket
        #----------------------------------------------------            
        else:
            # [thong bao] khoi tao thanh cong
            self.Ps.ServerMsg("on")
                
            # [thong bao] Lay dia chi IP
            self.Ps.msgServerOnline()

            # [thong bao] Server da san sang
            self.Ps.Line()

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
        Port=self.Port1
        if self.Server=="2":
            Port=self.Port2
        print Port
            
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect((self.Host, Port))
        except:
            return None
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



    # Xu li Recvdata chua thong so
    def ProcessData(self,server_socket,Tranf,sock,RecvData):
        #print "SOCKET_LIST ", SOCKET_LIST
        # Process User Login or Logout, And Broadcast to All User

        newserverSocket =server_socket
        newTranf        =Tranf
        newSock         =sock

        if "#user" in RecvData:
            # Anh xa Socket <-> User
            NewNickName = RecvData.split(":")[1].strip()
            for key,value in NickName.items():
                #print key,value
                if NewNickName in value:
                    NewNickName=value+str(1)
                    
            NickName[newSock.getpeername()] = NewNickName               

            #print self.msg.msg2
            msgUsr=self.Ps.MsgNewUser(newSock, NewNickName,self.Server)

            # Dem so luong user
            countUser=self.Ps.MsgCountUser(NickName)

            MessageContent = msgUsr[1]
            print msgUsr[0]

            print countUser
            
            #self.broadcast(neMsgCountUser(self,NickName)wserverSocket, newSock, MessageContent)
            self.SendtoClient(newserverSocket, newTranf, newSock, MessageContent)
            self.SendtoClient(newserverSocket, newTranf, newSock, countUser)
	    #self.server.broadcast(server_socket, sock, MessageContent)

        elif "#exit" in RecvData:
            
            try:
                msgUsrLogout = self.Ps.MsgUserLogout(NickName,newSock)
                
            except:
                print "Error when exit"
            
            else:
                # send data to Client
                MessageContent = msgUsrLogout[1]


                # Remove User From UserList
                self.Ps.RemoveNickName(NickName,newSock)

                # Dem so luong user
                countUser=self.Ps.MsgCountUser(NickName)

		# [Thong bao] Thong tin User
                print msgUsrLogout[0]

		# [Thong bao] Dem so luong user hien tai
                print countUser
            
                self.broadcast(newserverSocket, newSock, MessageContent)
                self.broadcast(newserverSocket, newSock, countUser)
                SOCKET_LIST.remove(newSock)


        #Recv Data And Broadcast to All User
        else:
            #print RecvData
            try:
                MessageContent = self.Ps.ProcessRecvData(NickName,newSock,RecvData)
                self.broadcast(newserverSocket, newSock, MessageContent)
                print MessageContent
            except:
                pass
