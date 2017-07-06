#process
# -*- coding: utf-8 -*-
import time

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

    def ServerMsg(self, Mode, PORT):
        MessageContent = ""
        NewTime = self.getCurrentDateTime('d')

        if (Mode == 'on'):
            MessageContent = """
            """ + NewTime + """
            Server Đang mở, Port """ + str(PORT) + """


            """

        elif (Mode == 'off'):
            MessageContent = """

            """ + NewTime + """
            Server Đã đóng, Port """ + str(PORT) + """


            """
        return MessageContent

    def show(self, MessageContent):
        print MessageContent


class Msg:
    def __init__(self):
        P = Process()
        self.msg1= "[ " + P.getCurrentDateTime('t') + "]- [AUTO] [ADMIN*THAI] : Chào mừng đến với phòng chat :)"
        self.msg2= """
        Đêm nay thật buồn, vì anh biết em đang ở nơi rất xa 
        Một nơi mà anh không thể đến được bên em ngay trong lúc này 
        Nhưng dù cho đó là nơi nào, một khi con tim chúng ta còn thuộc về nhau 
        Anh không cảm thấy cô đơn nhưng rất buồn vì nhớ em. 
    
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

