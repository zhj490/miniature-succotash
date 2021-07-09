from power2 import Power2
from power1 import Power1
import serial
import time
from receiever import Receiever


# from time import sleep

class Comm:
    def __init__(self, key1, str):
        self.ser = serial.Serial(str, 9600, timeout=0.5)  # /dev/ttyUSB
        self.key1 = key1
        self.mon = Receiever('COM4',9600) #接收来自打印机的信号端口以及波特率

    def G(self, key2, value=0.0):

        if (self.key1 == 1):
            if (key2 == 0):
                self.ser.write(Power1.end(self, ))
                time.sleep(0.01)

            if (key2 == 1):
                self.ser.write(Power1.start(self, ))
                time.sleep(0.01)
            if (key2 == 2):
                # Power2.setI(self,value)
                self.ser.write(Power1.setI(self, value))
                time.sleep(0.01)
            if (key2 == 3):
                self.ser.write(Power1.setV(self, value))
                time.sleep(0.01)

        if (self.key1 == 2):
            if (key2 == 0):
                self.ser.write(Power2.end(self, ))
                time.sleep(0.01)

            if (key2 == 1):
                self.ser.write(Power2.start(self, ))
                time.sleep(0.01)
            if (key2 == 2):
                # Power2.setI(self,value)
                self.ser.write(Power2.setI(self, value))
                time.sleep(0.01)
            if (key2 == 3):
                self.ser.write(Power2.setV(self, value))
                time.sleep(0.01)

    def monitor(self):
        self.mon.rec()

    def shut(self):
        self.ser.close()


if __name__ == '__main__':
    t1 = Comm(1, 'COM6')  # 参数1表示电源标识，参数2表示端口
    t1.G(3, 20)
    t1.G(2, 2)
    t1.monitor()
    #time.sleep(10)
    #t1.G(0)
    t1.shut()
    time.sleep(1)
    # t2 = Comm(2,'COM4')  #参数1表示电源标识，参数2表示端口
    # t2.G(1)
    # time.sleep(10)
    # t2.G(2,20.12)
    # time.sleep(10)
    # t2.G(3,100)
    # time.sleep(10)
    # t2.shut()