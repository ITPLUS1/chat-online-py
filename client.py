# chat_client.py

import sys
import socket
import select
import time
import os

DestPath="/root/Desktop/"
def checkFileExist(sourcePath):
    try:
        sF=open(sourcePath)
    except:
        return False
    else:
        return True

def StoreToFile(FileName,DestPath,Data):
    DestPath+=FileName
    print "DestPath",DestPath

    if checkFileExist(DestPath):
	os.system("mv "+DestPath+" "+DestPath+".bak")
    
    try:
        sF=open(DestPath,'wb')

    except:
	print "Fail to Store File"
    else:
        sF.write(str(Data))
	sF.close()

def getCurrentDateTime(mode):
    try:
        if mode=='t':
            return time.strftime("%H:%M")
        elif mode=='d':
            return time.strftime("%d-%m-%Y")
    except:
        return ""


def chat_client():
    os.system('clear')
    if(len(sys.argv) < 3) :
        print 'Usage : python chat_client.py hostname port'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    command=''     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()

    try:
        print 'Connected to remote host. You can start sending messages'
	print '#exit: Logout\n\n'
	
        name=raw_input("Enter NickName: ")
        s.send("#user:"+name)
    
        #sys.stdout.write('['+getCurrentDateTime('t')+'][Me] '); sys.stdout.flush()
     	sys.stdout.write('>'); sys.stdout.flush()

        while 1:
            socket_list = [sys.stdin, s]
         
            # Get the list sockets which are readable
            ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
            for sock in ready_to_read:             
                if sock == s:
                    # incoming message from remote server, s
                    data = sock.recv(4096)
                    if not data :
                        print '\nDisconnected from chat server'
                        sys.exit()

                    else :
                        sys.stdout.write(data+'\n>');
	    	        sys.stdout.flush()

			#StoreToFile(FileName,DestPath,data)
    
            
                else :

                    # user entered a message
                    sys.stdout.write('>'); sys.stdout.flush() 
                    msg = sys.stdin.readline()
		    command=msg
                    s.send(msg)

            if '#exit' in command:
                    print "GoodBye!!!"
                    sys.exit()


    except KeyboardInterrupt:
        print "\nClose Chat!!!"
if __name__ == "__main__":
    print getCurrentDateTime('d')
    sys.exit(chat_client())
