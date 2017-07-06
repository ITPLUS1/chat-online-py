# chat_client.py
# -*- coding: utf-8 -*-

import sys
import socket
import select
import os
import time

sys.path.append("BLL")
from Client_BLL import *
from Process import *

timeout=2
class clientChat:
    def __init__(self):
        print "\nChào mừng đến với phần mềm chat online X\n"

    def chat_client(self):
        #os.system('clear')
        if(len(sys.argv) < 3) :
            print 'Cú pháp : python client.py [Server] [cổng]'
            sys.exit()

        host = sys.argv[1]
        port = int(sys.argv[2])
        command=''
        Cl=Client()
        s=Cl.ConnectServer(timeout)
        try:
            if s:
                if Cl.TrytoConnect(s,host,port):
                    #print s,host,port
                    print 'Kết nối đến mày chủ thành công, Bây giờ bạn có thể chém gió '
                    print '#exit: Thoát \n\n'
                    name=raw_input("Nhập NickNam3: ")
                    s.send("#user:"+name)
                    #sys.stdout.write('['+getCurrentDateTime('t')+'][Me] '); sys.stdout.flush()
                    sys.stdout.write('>'); sys.stdout.flush()
                    while 1:
                        socket_list = [sys.stdin, s]
                        #print "socket_list ",socket_list

                        # Get the list sockets which are readable
                        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
                        #print "ready_to_read ",ready_to_read
                        for sock in ready_to_read:
                            Cl.StreamData(sock,s)
                else:
                    os.system('clear')
                    print "\nKhông thể kết nối đến Server\n"


        except KeyboardInterrupt:
            print "\nĐóng chat!!!"
if __name__ == "__main__":
    chat=clientChat()
    sys.exit(chat.chat_client())
