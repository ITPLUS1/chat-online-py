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



    def BindServer(self,Port=4444,MaxClient=10):
        self.Port=Port
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.Host, Port))
        server_socket.listen(MaxClient)
        return server_socket


    # broadcast chat messages to all connected clients
    def broadcast(self,server_socket, sock, message):
        for socket in SOCKET_LIST:
            #send the message only to peer
            if socket != server_socket and socket != sock:
                try:
                    socket.send(message)
                except:
                    # broken socket connection
                    socket.close()
                    # broken socket, remove it
                    if socket in SOCKET_LIST:
                        SOCKET_LIST.remove(socket)

    def TranferToClient(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        try:
            s.connect((self.Host, self.Port))
        except:
            SOCKET_LIST.remove(socket)
        else:
            return s



    def SendtoClient(self,server_socket,Tranf,sock,message):
        for socket in SOCKET_LIST:
            #send the message only to peer
            if socket != server_socket and socket != Tranf:
                try:
                    socket.send(message)
                except:
                    # broken socket connection
                    socket.close()
                    # broken socket, remove it
                    if socket in SOCKET_LIST:
                        SOCKET_LIST.remove(socket)

    def MsgNewUser(self,sock, NewNickName):
        MessageContent=[]
        Message = "[ " + self.Ps.getCurrentDateTime('t') + " ]- *****Chào mừng thành viên: "+NewNickName+" đã vào phòng chat"
        MessageContent.append(str(sock.getpeername()) + Message)
        MessageContent.append(Message)
        return MessageContent


    def MsgUserLogout(self, sock):
        MessageContent = []
        Message = "[ " + self.Ps.getCurrentDateTime('t') + " ]- ***** Thành viên: "+NickName[sock.getpeername()] + " Đã thoát!!!"
        MessageContent.append(NickName[sock.getpeername()] + Message)
        MessageContent.append(Message)
        return MessageContent

    def ProcessRecvData(self,sock,RecvData):
        MessageContent = "[ " + self.Ps.getCurrentDateTime('t') + "]- "+ NickName[sock.getpeername()] + " - " + RecvData.strip().replace("\r\n","")
        #print "RecvData - MessageContent ",MessageContent
        return MessageContent

    def ProcessData(self,server_socket,Tranf,sock,RecvData):
        #print "SOCKET_LIST ", SOCKET_LIST
        # Process User Login or Logout, And Broadcast to All User
        newSock         =sock
        newserverSocket =server_socket
        newTranf        =Tranf
        if "#user" in RecvData:
            try:
                NewNickName = RecvData.split(":")[1].strip()
                NickName[newSock.getpeername()] = NewNickName

            except:
                pass

            else:
                #print self.msg.msg2
                msgUsr=self.MsgNewUser(newSock, NewNickName)
                MessageContent = msgUsr[1]
                print msgUsr[0]
                #self.broadcast(newserverSocket, newSock, MessageContent)

                #self.SendtoClient(newserverSocket, newTranf, newSock,self.msg.msg1 )
                self.SendtoClient(newserverSocket, newTranf, newSock, MessageContent)

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


