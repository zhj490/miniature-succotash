from power2 import Power2
from power1 import Power1
import serial
import time
from receiever import Receiever


# from time import sleep

class Comm1:
    ser3 = serial.Serial('COM4',9600)#接收来自打印机的信号端口以及波特率
    ser3.flushInput()

    def __init__(self,key1 = 1 ,str1 = '',key2 = 2,str2 = ''):
        self.ser1 = serial.Serial(str1, 9600, timeout=0.5)
        self.ser2 = serial.Serial(str2, 9600, timeout=0.5)
        self.key1 = key1
        self.key2 = key2
        #self.mon = Receiever('COM4',9600) #接收来自打印机的信号端口以及波特率

    def G(self,key,key3, value=0.0):

        if (key == self.key1):
            if (key3 == 0):
                self.ser1.write(Power1.end(self, ))
                time.sleep(0.01)

            if (key3 == 1):
                self.ser1.write(Power1.start(self, ))
                time.sleep(0.01)
            if (key3 == 2):
                # Power2.setI(self,value)
                self.ser1.write(Power1.setI(self, value))
                time.sleep(0.01)
            if (key3 == 3):
                self.ser1.write(Power1.setV(self, value))
                time.sleep(0.01)

        if (key == self.key2):
            if (key3 == 0):
                self.ser2.write(Power2.end(self, ))
                time.sleep(0.01)

            if (key3 == 1):
                self.ser2.write(Power2.start(self, ))
                time.sleep(0.01)
            if (key3 == 2):
                # Power2.setI(self,value)
                self.ser2.write(Power2.setI(self, value))
                time.sleep(0.01)
            if (key3 == 3):
                self.ser2.write(Power2.setV(self, value))
                time.sleep(0.01)

    def monitor(self):
        while True:
            count = Comm1.ser3.inWaiting()  # 获取串口缓冲区数据
            if count != 0:
                recv = Comm1.ser3.read(Comm1.ser3.in_waiting)
                if(recv == b'11'): #前一个数表示电源1，后一个数表示电源2
                    self.ser1.write(Power1.start(self))
                    #self.ser.write(Power2.start(self))
                    print("hello")
                if(recv == b'01'):
                    self.ser1.write(Power1.start(self))
                    #self.ser.write(Power2.end(self))
                    print("world")
                if (recv == b'10'):  # 前一个数表示电源1，后一个数表示电源2
                    self.ser1.write(Power1.start(self))
                    #self.ser.write(Power2.end(self))
                    print("nihao")
                if (recv == b'00'):
                    self.ser1.write(Power1.end(self))
                    #self.ser.write(Power2.end(self))
                    print("shijie")
                #print(time.time(), "---recv--->", recv)
                #print(recv[0])
                #time.sleep(0.1)  # 延时0.1s

    def shut(self):
        self.ser1.close()
        self.ser2.close()


#if __name__ == '__main__':
    #t1 = Comm1(1, 'COM6')  # 参数1表示电源标识，参数2表示端口
    #t1.G(3, 20)
    #t1.G(2, 2)
    #t1.monitor()
    #time.sleep(10)
    #t1.G(0)
    #t1.shut()
    #time.sleep(1)
    # t2 = Comm(2,'COM4')  #参数1表示电源标识，参数2表示端口
    # t2.G(1)
    # time.sleep(10)
    # t2.G(2,20.12)
    # time.sleep(10)
    # t2.G(3,100)
    # time.sleep(10)
    # t2.shut()