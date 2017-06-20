import socket
import time
SOCKET_LIST    = []
server_socket=None


class Server(object):
    MaxClient=0
    Port=0
    Host=''

    def __init__(self,Port,MaxClient):
        global server_socket
        self.Port       =Port
        self.MaxClient  =MaxClient


    def BindServer(self):
        # type: () -> object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.Host, self.Port))
        server_socket.listen(self.MaxClient)
        return server_socket

        #return server_socket
        # broadcast chat messages to all connected clients


    def ShowMessage(self):
        Welcome_Msg = "\n-----------------Welcome to chatting room : "
        Bye_Msg = "\n-----------------Goodbye : "




    def broadcast(self,server_socket, sock, message):
        global SOCKET_LIST
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


    def SendtoClient(self,server_socket, sock,usr,Mode):
        global SOCKET_LIST
        for socket in SOCKET_LIST:
            #send the message only to peer
            if socket != server_socket and socket == sock and Mode == 'hello':
                NewMsg=self.ShowMessage.Welcome_Msg+usr
                print NewMsg
                try:
                    server_socket.send(NewMsg)
                except:
                    # broken socket connection
                    #socket.close()
                    # broken socket, remove it
                    if socket in SOCKET_LIST:
                        SOCKET_LIST.remove(socket)




class Process:
    def __init__(self):
        print ''

    def getCurrentDateTime(self,mode):
        try:
            if mode=='t':
                return time.strftime("%H:%M")
            elif mode=='d':
                return time.strftime("%d-%m-%Y")
        except:
            return None



    def show(self,MessageContent):
            print MessageContent
