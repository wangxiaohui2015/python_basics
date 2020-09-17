import threading
import time


class MyThread(threading.Thread):
    def __init__(self, id, delay):
        self.__id = id
        self.__delay = delay
        super().__init__()

    def run(self):
        for i in range(3):
            print("%s hello %d ... %s" % (self.__id, i, time.ctime(time.time())))
            time.sleep(self.__delay)


t1 = MyThread(1, 1)
t2 = MyThread(2, 2)

t1.start()
t2.start()

t1.join()
t2.join()

print("main end.")
