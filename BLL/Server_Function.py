import socket

class Bind_Chat_Server(object):
    MaxClient=0
    Port=0
    Host=''

    def __init__(self):
        print ''

    def Make(self,Port,MaxClient):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.Host, Port))
        server_socket.listen(MaxClient)
        return server_socket
        # broadcast chat messages to all connected clients

    def broadcast(self,server_socket, sock, message,SOCKET_LIST):
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