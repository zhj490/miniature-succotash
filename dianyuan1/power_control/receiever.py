import time
import serial
from power2 import Power2
from power1 import Power1



class Receiever:
    def __init__(self,port,baudrate):
        self.ser = serial.Serial(port,baudrate,)
        self.ser.flushInput()  # 清空缓冲区




    def rec(self):
        while True:
            count = self.ser.inWaiting()  # 获取串口缓冲区数据
            if count != 0:
                recv = self.ser.read(self.ser.in_waiting)
                if(recv == b'11'): #前一个数表示电源1，后一个数表示电源2
                    self.ser.write(Power1.start(self))
                    #self.ser.write(Power2.start(self))
                    print("hello")
                if(recv == b'01'):
                    self.ser.write(Power1.start(self))
                    #self.ser.write(Power2.end(self))
                    print("world")
                if (recv == b'10'):  # 前一个数表示电源1，后一个数表示电源2
                    self.ser.write(Power1.start(self))
                    #self.ser.write(Power2.end(self))
                    print("nihao")
                if (recv == b'00'):
                    self.ser.write(Power1.end(self))
                    #self.ser.write(Power2.end(self))
                    print("shijie")
                #print(time.time(), "---recv--->", recv)
                #print(recv[0])
                #time.sleep(0.1)  # 延时0.1s


if __name__ == '__main__':
    a = Receiever('COM4',9600)
    a.rec()
