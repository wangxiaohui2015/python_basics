import threading
import time

LOCK = threading.Lock()


def say_hello(id, delay):
    LOCK.acquire()
    for i in range(5):
        print("%s hello %d ... %s" % (id, i, time.ctime(time.time())))
        time.sleep(delay)
    LOCK.release()


t1 = threading.Thread(target=say_hello, args=(1, 1))
t2 = threading.Thread(target=say_hello, args=(2, 2))

t1.start()
t2.start()

t1.join()
t2.join()

print("main end.")
