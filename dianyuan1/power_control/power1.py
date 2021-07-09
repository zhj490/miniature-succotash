class Power1:
    def __init__(self):
        self.b1 = ['AA', '01', '21', '02', '00', '00', '00']
        self.b2 = ['AA', '01', '22', '02', '00', '00', '00']
        self.b3 = ['AA', '01', '20', '01', '01', '23']
        self.b4 = ['AA', '01', '20', '01', '00', '22']

    def setV(self, num):

        if (num >= 0.00 and num <= 60.00):
            num = int(num * 100)
            self.b1 = ['AA', '01', '21', '02', '00', '00', '00']
            b = "{:02X}".format(num // 256 % 256)
            c = "{:02X}".format(num % 256)
            d = "{:02X}".format((36 + num // 256 % 256 + num % 256) % 256)

            # print(d1)
            # print(b1)
            self.b1[4] = c
            self.b1[5] = b
            self.b1[6] = d
            A1 = [0, 0, 0, 0, 0, 0, 0]
            for i in range(7):
                A1[i] = int(self.b1[i], 16)
            return A1
        else:
            print("1的电压参数超出范围")

    def setI(self, num):

        if (num >= 0.00 and num <= 20.00):
            num = int(num * 100)
            self.b2 = ['AA', '01', '22', '02', '00', '00', '00']
            b = "{:02X}".format(num // 256 % 256)
            c = "{:02X}".format(num % 256)
            d = "{:02X}".format((37 + num // 256 % 256 + num % 256) % 256)
            # print(b)
            # print(c)
            self.b2[4] = c
            self.b2[5] = b
            self.b2[6] = d
            A2 = [0, 0, 0, 0, 0, 0, 0]
            for i in range(7):
                A2[i] = int(self.b2[i], 16)
            return A2
        else:
            print("1的电流参数超出范围")

    def start(self):
        self.b3 = ['AA', '01', '20', '01', '01', '23']
        A3 = [0, 0, 0, 0, 0, 0]
        for i in range(6):
            A3[i] = int(self.b3[i], 16)
        return A3

    def end(self):
        self.b4 = ['AA', '01', '20', '01', '00', '22']
        A4 = [0, 0, 0, 0, 0, 0]
        for i in range(6):
            A4[i] = int(self.b4[i], 16)
        return A4


if __name__ == '__main__':
    t = Power1()
    print(t.setV(10))
    print(t.setI(0.5))