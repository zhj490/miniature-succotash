from crc16 import PyModBus


class Power2:
    def __init__(self):
        self.a1 = ['01', '10', '00', '40', '00', '02', '04', '00', '00', '00', '00', '00', '00']
        self.a2 = ['01', '10', '00', '41', '00', '02', '04', '00', '00', '00', '00', '00', '00']
        self.a3 = ['01', '10', '00', '42', '00', '02', '04', '00', '00', '00', '00', '00', '00']

    def setV(self, num):
        if (num >= 0.00 and num <= 200.00):
            num = int(num * 100)
            MyModBus = PyModBus()
            self.a1 = ['01', '10', '00', '40', '00', '02', '04', '00', '00', '00', '00', '00', '00']
            b = "{:02X}".format(num // 256 % 256)
            c = "{:02X}".format(num % 256)
            self.a1[9] = b;
            self.a1[10] = c;
            b = "{:02X}".format(MyModBus.crc16(0, 11, self.a1[:]) // 256 % 256)
            c = "{:02X}".format(MyModBus.crc16(0, 11, self.a1[:]) % 256)
            self.a1[11] = b;
            self.a1[12] = c;
            A1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(13):
                A1[i] = int(self.a1[i], 16)
            return A1
        else:
            print("2的电压参数超出范围")

    def setI(self, num):
        if (num >= 0.00 and num <= 50.00):
            num = int(num * 100)
            MyModBus = PyModBus()
            self.a2 = ['01', '10', '00', '41', '00', '02', '04', '00', '00', '00', '00', '00', '00']
            b = "{:02X}".format(num // 256 % 256)
            c = "{:02X}".format(num % 256)
            self.a2[9] = b;
            self.a2[10] = c;
            b = "{:02X}".format(MyModBus.crc16(0, 11, self.a2[:]) // 256 % 256)
            c = "{:02X}".format(MyModBus.crc16(0, 11, self.a2[:]) % 256)
            self.a2[11] = b;
            self.a2[12] = c;
            A2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(13):
                A2[i] = int(self.a2[i], 16)
            return A2
        else:
            print("2的电流参数超出范围")

    def start(self):
        self.a3 = ['01', '10', '00', '42', '00', '02', '04', '00', '00', '00', '01', 'B7', '86']
        A3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(13):
            A3[i] = int(self.a3[i], 16)
        return A3

    def end(self):
        self.a3 = ['01', '10', '00', '42', '00', '02', '04', '00', '00', '00', '00', '76', '46']
        A3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(13):
            A3[i] = int(self.a3[i], 16)
        return A3


if __name__ == '__main__':
    MyPower2 = Power2()
    MyPower2.setV(200)
    print(MyPower2.setI(13))
    print(MyPower2.a2)
