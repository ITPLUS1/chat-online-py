import socket

class Bind_Chat_Server(object):
    HOST = ''
    RECV_BUFFER = 4096
    def __init__(self,Port,MaxClient):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.HOST, Port))
        server_socket.listen(MaxClient)
