# -*- coding:utf-8 -*-

# RLock and Lock

import threading
from time import sleep

class Counter:

    def __init__(self):
        self.__count = 0
        self.__lock = threading.RLock()
        #self.__lock = threads.Lock() # Lock()不能在一个线程中被多次acquire，否则会进入死锁

    def Increase(self, threadNum):
        self.__lock.acquire()
        #self.__lock.acquire() # RLock()能够在一个线程中被多次acquire
        self.__count += 1
        sleep(1)
        print "%d: %d" % (threadNum, self.__count)
        #self.__lock.release() # RLock()只要acquire与release成对出现即可
        self.__lock.release()

if "__main__" == __name__:
    counter = Counter()
    threads = []
    for i in xrange(10):
        t = threading.Thread(target=counter.Increase, args=(i, ))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print "All threads end!!!"
