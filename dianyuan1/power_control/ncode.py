from commu import Comm
from time import sleep


class Ncode:
    def __init__(self, str1, str2):
        self.ser1 = Comm(1, str1)
        self.ser2 = Comm(2, str2)

    def N0(self, No1, num1, No2, num2, interval=0):
        self.ser1.G(No1, num1)
        self.ser2.G(No2, num2)
        sleep(interval)

    def N1(self, No1, num1=0, interval=0):
        self.ser1.G(No1, num1)
        sleep(interval)

    def N2(self, No2, num2=0, interval=0):
        self.ser2.G(No2, num2)
        sleep(interval)

    def shutUp(self, ):
        self.ser1.shut()
        self.ser2.shut()


if __name__ == '__main__':
    a = Ncode('COM3', 'COM4')
    a.N(1, 0, 2, 10, 5)
    a.N(1, 0, 2, 10, 5)