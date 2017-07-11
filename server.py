# chat_server.py
# -*- coding: utf-8 -*-

import os
import sys
import socket
import select
import time

sys.path.append("BLL")
from Server_BLL import *
from Process import *

#Nhan Dulieu
RECV_BUFFER = 4096

#BindServer
PORT        = 8888

#Tranfer Data
PORT2       = 8889

#Number Of CLient Connect
MaxClient   = 10


class ServerChat:
    def __init__(self):
        self.pr = Process()
        self.server = Server()

    def chat_server(self):
	# Tao Server
        server_socket       = self.server.BindServer(PORT, MaxClient)
        
	# Tao 1 Socket, [Ket noi den server de gui message to Client]
        #Tranf               = self.server.TranferToClient()

        # add server socket object to the list of readable connections
        # Them vao danh sach readable
        SOCKET_LIST.append(server_socket)
        #SOCKET_LIST.append(Tranf)

	# Thong bao
        MessageContent = self.pr.ServerMsg("on",PORT)
        self.pr.show(MessageContent)

        try:
            while 1:
                # get the list sockets which are ready to be read through select
                # 4th arg, time_out  = 0 : poll and never block
                ready_to_read, ready_to_write, in_error = select.select(SOCKET_LIST, [], [], 0)

                #print "SOCKET_LIST ", SOCKET_LIST
                #print "\nserver_socket ",server_socket
                #print "ready ",ready_to_read, ready_to_write, in_error
                #time.sleep(1)
                for sock in ready_to_read:
                    # a new connection request recieved
                    if sock == server_socket:

                        sockfd, addr = server_socket.accept()
                        #print "New conn: ",sockfd

			
			#Send data to new user
			#self.server.SendtoClient(server_socket,Tranf,sockfd,message)

			# Them vao List
                        SOCKET_LIST.append(sockfd)


                    # a message from a client, not a new connection
                    else:
                        # pr data recieved from client,
                        try:
                            # receiving data from the socket.
                            RecvData = sock.recv(RECV_BUFFER)
                            if RecvData:
                                #Process Data & Send to client
                                self.server.ProcessData(server_socket,Tranf,sock, RecvData)

                            else:
                                # remove the socket that's broken or client Logout
                                if sock in SOCKET_LIST:
                                    MessageContent = self.server.MsgUserLogout(sock)
                                    SOCKET_LIST.remove(sock)

                                    # at this stage, no data means probably the connection has been broken

                                self.server.broadcast(server_socket, sock, MessageContent)
                                continue

                        # exception
                        except:
                            MessageContent =self.server.MsgUserLogout(sock)
                            self.server.broadcast(server_socket, sock, MessageContent)
                            continue
        except:
            print "----------------------------------------------------------"
            MessageContent = self.pr.ServerMsg("off", PORT)
            self.pr.show(MessageContent)
            # print data_Stream
            # file_Store.write(data_Stream)
            # server_socket.close()
            # file_Store.close()


if __name__ == "__main__":
    chat2=ServerChat()
    sys.exit(chat2.chat_server())
