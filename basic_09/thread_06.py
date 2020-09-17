import threading
import time

LOCK = threading.RLock()


def say_hello(id, delay):
    LOCK.acquire()
    LOCK.acquire()  # Thread isn't blocked here because use RLock instead of Lock
    for i in range(3):
        print("%s hello %d ... %s" % (id, i, time.ctime(time.time())))
        time.sleep(delay)
    LOCK.release()
    LOCK.release()  # Invoke acquire 2 times, but invoked release 2 time, so thread 2 can go into say_hello()


t1 = threading.Thread(target=say_hello, args=(1, 1))
t2 = threading.Thread(target=say_hello, args=(2, 2))

t1.start()
t2.start()

t1.join()
t2.join()

print("main end.")
