import threading
import time


class MyBlockingQueue:
    def __init__(self, capacity):
        if capacity <= 0:
            self.__size = 10  # Default size is 10
        else:
            self.__capacity = capacity
        self.__lock = threading.RLock()
        self.__not_full = threading.Condition(self.__lock)
        self.__not_empty = threading.Condition(self.__lock)
        self.__data = []

    def offer(self, e):
        self.__lock.acquire()
        try:
            if len(self.__data) >= self.__capacity:
                self.__not_full.wait()
            self.__data.append(e)
            print("Append data: %r" % e)
            self.__not_empty.notify()
        except Exception as e:
            raise e
        finally:
            self.__lock.release()

    def poll(self):
        self.__lock.acquire()
        try:
            if len(self.__data) == 0:
                self.__not_empty.wait()
            e = self.__data.pop(0)
            self.__not_full.notify()
            return e
        except Exception as e:
            raise e
        finally:
            self.__lock.release()


class ReadDataThread(threading.Thread):
    def __init__(self, queue):
        self.__queue = queue
        super().__init__()

    def run(self):
        e = self.__queue.poll()
        print("Read data: %r" % e)


class WriteReadDataThread(threading.Thread):
    def __init__(self, queue, data):
        self.__queue = queue
        self.__data = data
        super().__init__()

    def run(self):
        self.__queue.offer(self.__data)


q = MyBlockingQueue(2)
wlist = []
rlist = []
for i in range(4):
    wlist.append(WriteReadDataThread(q, i))
    rlist.append(ReadDataThread(q))

for w in wlist:
    w.start()

for r in rlist:
    r.start()

print("Main end.")
