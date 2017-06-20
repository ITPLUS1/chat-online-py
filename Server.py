# chat_server.py
import sys

sys.path.append("BLL")
from Server_Function import *
import socket
import select
import time

#SOCKET_LIST    = []
server_socket   =0

PORT=8888
HOST=''
MAXCLIENT=10
RECV_BUFFER = 4096


class Server(object):
    def __init__(self):
            global HOST
            global PORT
            global SOCKET_LIST
            global server_socket
            global RECV_BUFFER

    def chat_server(self):
            server_socket_=Bind_Chat_Server()
            server_socket_
            server_socket=server_socket_.Make(PORT,MAXCLIENT)


            # add server socket object to the list of readable connections
            SOCKET_LIST.append(server_socket)

            print "Chat server started on port " + str(PORT)

            while 1:
                time.sleep(2)
                # get the list sockets which are ready to be read through select
                # 4th arg, time_out  = 0 : poll and never block
                ready_to_read, ready_to_write, in_error = select.select(SOCKET_LIST, [], [], 0)
                #print "SOCKET_LIST ",SOCKET_LIST
                print "ready_to_read ",ready_to_read
                for sock in ready_to_read:
                    # a new connection request recieved
                    if sock == server_socket:
                        sockfd, addr = server_socket.accept()
                        SOCKET_LIST.append(sockfd)
                        print "Client (%s, %s) connected" % addr
                        server_socket_.broadcast(server_socket, sockfd, "[%s:%s] entered our chatting room\n" % addr)
                        #broadcast(server_socket, sockfd, "[%s:%s] entered our chatting room\n" % addr)

                    # a message from a client, not a new connection
                    else:
                        # process data recieved from client,
                        try:
                            # receiving data from the socket.
                            data = sock.recv(RECV_BUFFER)
                            if data:
                                # there is something in the socket
                                #broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)
                                server_socket_.broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)
                            else:
                                # remove the socket that's broken
                                if sock in SOCKET_LIST:
                                    SOCKET_LIST.remove(sock)

                                # at this stage, no data means probably the connection has been broken
                                #broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                                server_socket_.broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)

                                # exception
                        except:
                            #broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                            server_socket_.broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                            continue

            server_socket.close()



if __name__ == "__main__":
        Server=Server()
        Server.chat_server()





