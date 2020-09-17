import threading
import time

LOCK = threading.Lock()


def say_hello(id, delay):
    LOCK.acquire()
    LOCK.acquire()  # Thread is blocked here, cannot invoke acquire 2 times unless release one
    for i in range(5):
        print("%s hello %d ... %s" % (id, i, time.ctime(time.time())))
        time.sleep(delay)
    LOCK.release()
    LOCK.release()


t1 = threading.Thread(target=say_hello, args=(1, 1))
t2 = threading.Thread(target=say_hello, args=(2, 2))

t1.start()
t2.start()

t1.join()
t2.join()

print("main end.")
