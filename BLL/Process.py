#process
# -*- coding: utf-8 -*-
import time
import socket
#get URL
import urllib

class Process:
    def __init__(self):
        pass

    def getCurrentDateTime(self, mode):
        try:
            if mode == 't':
                return time.strftime("%H:%M")
            elif mode == 'd':
                return time.strftime("%d-%m-%Y")
        except:
            return None

    # [Thong bao] Khoi tao server
    def msgServerBind(self, PORT):
        MessageContent = "\n\n"+bcolors.BOLD+bcolors.WARNING+"[ " + self.getCurrentDateTime('t') + "]- Khởi Tạo Server | CỔNG " +str(PORT)+bcolors.ENDC+"\n"
	print MessageContent


    def getPublicIP(self):
        try:
            ip = urllib.urlopen('http://icanhazip.com/').read().strip('\n')
        except:
            try:
                ipraw = urllib.urlopen('http://whatismyip.org').read().split("</span>")[1]
                ip2=ipraw.split(">")[-1]
            except:
                return None
                
            else:
                #print "ip2",ip2
                return ip2
        else:
            #print "ip1",ip
            return ip
        return None

    def getLocalIP(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('google.com', 0))
            ip=s.getsockname()[0]
            return ip
        except:
            return None


    def Line(self):
        print """

            đã sẵn sàng kết nối
            

        """
        print "-"*120

    # [Thong bao] Tinh trang server
    def msgServerOnline(self):
        MessageWait = bcolors.BOLD+bcolors.WARNING+"[ " + self.getCurrentDateTime('t') + "]- Đang lấy IP..."+bcolors.ENDC
        print MessageWait
        
        publicIP=self.getPublicIP()
        localIP=self.getLocalIP()


        Status="Offline!!!"
        if(publicIP != None):
            Status="Online"
        else:
            publicIP=""


        if(localIP == None):
            localIP=""

    
        MessageContent = bcolors.BOLD+bcolors.WARNING+"[ " + self.getCurrentDateTime('t') + "]- Server "+Status+bcolors.ENDC+"\n"
        MessageContent2 = " Public IP: "+publicIP+"\n"+" LOcal IP: "+localIP+"\n"
        
	print MessageContent
	print MessageContent2



    # [Thong bao] Server ban
    def msgServerBusy(self, PORT):
        MessageContent = bcolors.BOLD+bcolors.FAIL+"[ " + self.getCurrentDateTime('t') + "]- SERVER ĐANG BẬN, THỬ CỔNG " +str(PORT)+bcolors.ENDC+"\n"
	print MessageContent

    # [Thong bao] Server Loi
    def msgServerError(self, PORT):
        MessageContent = bcolors.BOLD+bcolors.FAIL+"[ " + self.getCurrentDateTime('t') + "]- KHÔNG THỂ TẠO SERVER " +str(PORT)+bcolors.ENDC+"\n"
	print MessageContent


    # [Thong bao] Thong tin Server 
    def ServerMsg(self, Mode):
        MessageContent = ""
        NewTime = self.getCurrentDateTime('t')

        if (Mode == 'on'):
            MessageContent = bcolors.BOLD+bcolors.WARNING+"[ " + self.getCurrentDateTime('t') +"]- Server Đã mở" +bcolors.ENDC+"\n"

        elif (Mode == 'off'):
            MessageContent = bcolors.BOLD+bcolors.FAIL+"[ " + self.getCurrentDateTime('t') + "]- Server Đã đóng " +bcolors.ENDC+"\n"
        print MessageContent

    def show(self, MessageContent):
        print MessageContent


    #Xoa user ra khoi danh sach
    def RemoveNickName(self, NickName,sock):
        NickNameList=NickName
        User=NickNameList[sock.getpeername()]
        for key,value in NickNameList.items():
            if value==User:
                NickNameList.pop(key)
            
        return NickNameList        



    # [Thong bao] dem so thanh vien hien co
    def MsgCountUser(self,NickName):
        ListUser=[]
        Count=0
        for key,value in NickName.items():
            Count+=1
            ListUser.append(value)
            
        ListUser=",".join(ListUser)
            
        MessageContent= bcolors.BOLD+bcolors.OKBLUE + "[ " + self.getCurrentDateTime('t') + " ]"+bcolors.ENDC+bcolors.OKGREEN+"- Thành viên đang online: "+str(Count)+"\n\t\t"+ListUser+bcolors.ENDC+"\n"
        return MessageContent

    # [Thong bao] den new user
    def MsgNewUser(self,sock,NewNickName,Server):
        MessageContent=[]
        msgShow= bcolors.BOLD+bcolors.OKBLUE + "[ " + self.getCurrentDateTime('t') + " ]"+bcolors.ENDC+"-[ New Socket ] "+str(sock.getpeername())+"\n"
        Message =bcolors.BOLD+bcolors.OKBLUE + "[ " + self.getCurrentDateTime('t') + " ]"+bcolors.ENDC+bcolors.OKGREEN+"- [ SERVER "+Server+" ]*****Chào mừng thành viên: "+NewNickName+" đã vào phòng chat"+bcolors.ENDC+"\n"
        MessageContent.append(msgShow+ Message)
        MessageContent.append(Message)
        return MessageContent


    # [Thong bao] trung ten new user
    def MsgUserExist(self,sock,NewNickName):
        MessageContent=[]
        Message = "[ " + self.getCurrentDateTime('t') + " ]- #Tên : "+NewNickName+" đã tồn tại, vui lòng nhập tên khác"
        MessageContent.append(str(sock.getpeername()) + Message)
        MessageContent.append(Message)
        return MessageContent



    # [Thong bao] den user [Logout] huac mat ket noi
    def MsgUserLogout(self, NickName,sock):
        MessageContent = []
        Message = bcolors.BOLD+bcolors.OKBLUE+"[ " + self.getCurrentDateTime('t') + " ]"+bcolors.ENDC+bcolors.FAIL+"- ***** Thành viên: "+NickName[sock.getpeername()] + " Đã thoát!!!"+bcolors.ENDC+"\n"
        MessageContent.append(NickName[sock.getpeername()] + Message)
        MessageContent.append(Message)
        return MessageContent

    # [Thong bao] Message [Nhan duoc] tu user
    def ProcessRecvData(self,NickName,sock,RecvData):
        MessageContent = bcolors.BOLD+bcolors.OKBLUE+"[ " + self.getCurrentDateTime('t') + " ]"+bcolors.ENDC+bcolors.White+"- "+ NickName[sock.getpeername()] + " - " + RecvData.strip().replace("\r\n","")
        #print "RecvData - MessageContent ",MessageContent
        return MessageContent











class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'

    Purple='\033[0;35m'       # Purple
    Cyan='\033[0;36m'         # Cyan
    White='\033[0;97m'        # White
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



class Msg:
    def __init__(self):
        P = Process()
        self.msg1= "[ " + P.getCurrentDateTime('t') + "]- [AUTO] [ADMIN*THAI] : Chào mừng đến với phòng chat :)"
        self.msg2= """
        Đường phố thinh lặng, 
        Chỉ còn cơn gió thoáng đưa một chút sương lạnh 
        Làm buốt vai anh, chợt thấy đêm dài, 
        Vì lòng thao thức muốn nghe từng phút cô đơn 
        Khẽ trôi bềnh bồng. 
    
        Và nghe em như kề bên 
        Vòng tay thơ ấm êm 
        Nói cười với anh 
        Và nghe sâu trong lòng anh 
        Yêu thương gọi tên em giữa khuya. 
    
        Tình yêu đốt cháy tim này, trong một phút mong chờ 
        Lạc trong đêm bên nỗi nhớ, lạnh đôi vai se buốt giá 
        Ngoài kia phố vắng hiu quạnh, nơi tận cuối con đường 
        Một người ngu ngơ bước đi, tìm quanh đâu đây bóng em
        """

