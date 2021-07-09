from commu1 import Comm1
import time


t = Comm1(1, 'COM6',2,'COM1')  # 参数1表示电源标识，参数2表示端口
t.G(1,3,20)
t.G(2,3,20)
time.sleep(2)
t.G(1,2,2)
t.G(2,2,2)
time.sleep(2)
t.monitor()
# time.sleep(10)
# t1.G(0)
t.shut()
time.sleep(1)