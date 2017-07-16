# chat_client.py
# -*- coding: utf-8 -*-
########################################
# Write by IT PLUS TEAM
########################################
import sys
import socket
import select
import os
import time

sys.path.append("BLL")
from Client_BLL import *
from Process_BLL import *

timeout=2
class clientChat:
    def __init__(self):
        print """


	\nChào mừng đến với chat online X


	"""

    def chat_client(self):
        #os.system('clear')
        if(len(sys.argv) < 3) :
            print bcolors.BOLD+bcolors.FAIL+'Cú pháp : python client.py [Server] [cổng]'+bcolors.ENDC+"\n\n"
            sys.exit()

        host = sys.argv[1]
        port = int(sys.argv[2])
        command=''
        Cl=Client()
        
        # Khoi tao socket
        s=Cl.ConnectServer(timeout)
        try:
            if s:
                # Ket noi den Server
                if Cl.TrytoConnect(s,host,port):
                    print bcolors.BOLD+bcolors.OKBLUE + 'Kết nối đến máy chủ thành công, Bây giờ bạn có thể chém gió '+ 		bcolors.ENDC
                    print bcolors.BOLD+bcolors.FAIL+'#exit: Thoát \n\n'+bcolors.ENDC
                    name=raw_input("Nhập NickNam3: ")
                    
                    #Gui ten username den server
                    s.send("#user:"+name)
                    
                    sys.stdout.write('>'); sys.stdout.flush()
                    while 1:
                        # Nhan du lieu tu keyboard
                        socket_list = [sys.stdin, s]

                        # Get the list sockets which are readable
                        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])

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
