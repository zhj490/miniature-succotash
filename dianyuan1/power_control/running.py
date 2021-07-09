import time
from commu import Comm
from multiprocessing import Process


def func_one():
    print('hello')
    time.sleep(5)
    print('bye')
    time.sleep(5)
    print('hello')
    time.sleep(5)
    print('bye')


def func_two():
    t2 = Comm(1, 'COM4')  # 参数1表示电源标识，参数2表示端口
    t2.G(3, 50)
    time.sleep(5)
    t2.G(2, 20)
    time.sleep(5)
    t2.G(1)
    time.sleep(5)
    t2.G(0)
    time.sleep(5)
    t2.shut()


if __name__ == '__main__':
    p_one = Process(target=func_one, )
    p_two = Process(target=func_two, )
    p_one.start()
    p_two.start()
    # p_one.join()
    # p_two.join()