# chat_server.py
import sys

sys.path.append("BLL")
from Server_Function import *
import socket
import select

SOCKET_LIST = []
server_socket=''

class Server(object):
    def __init__(self):
        self.Port       = 4444
        self.MaxClient  = 1

        global server_socket
        server_socket = Bind_Chat_Server(self.Port, self.MaxClient)

    def chat_server(self):
        global SOCKET_LIST
        #add server socket object to the list of readable connections
        SOCKET_LIST.append(server_socket)
        print SOCKET_LIST
        print "Chat server started on port " + str(self.Port)

        while 1:
            # get the list sockets which are ready to be read through select
            # 4th arg, time_out  = 0 : poll and never block
            ready_to_read, ready_to_write, in_error = select.select(SOCKET_LIST, [], [], 1)

            for sock in ready_to_read:
                # a new connection request recieved
                if sock == server_socket:
                    sockfd, addr = server_socket.accept()
                    SOCKET_LIST.append(sockfd)
                    print "Client (%s, %s) connected" % addr

                    broadcast(server_socket, sockfd, "[%s:%s] entered our chatting room\n" % addr)

                # a message from a client, not a new connection
                else:
                    # process data recieved from client,
                    try:
                        # receiving data from the socket.
                        data = sock.recv(RECV_BUFFER)
                        if data:
                            # there is something in the socket
                            broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)
                        else:
                            # remove the socket that's broken
                            if sock in SOCKET_LIST:
                                SOCKET_LIST.remove(sock)

                            # at this stage, no data means probably the connection has been broken
                            broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)

                            # exception
                    except:
                        broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                        continue

        server_socket.close()


    # broadcast chat messages to all connected clients
    def broadcast(server_socket, sock, message):
        for socket in SOCKET_LIST:
            # send the message only to peer
            if socket != server_socket and socket != sock:
                try:
                    socket.send(message)
                except:
                    # broken socket connection
                    socket.close()
                    # broken socket, remove it
                    if socket in SOCKET_LIST:
                        SOCKET_LIST.remove(socket)


if __name__ == "__main__":
    Server=Server()
    Server.chat_server()