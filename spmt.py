# -*- coding:utf-8 -*-

# single process multi thread (spmt)

import threading
from time import ctime, sleep

class Entertainment:

    def music(self, name):
        for i in xrange(10):
            print "%s listen music %s" % (ctime(), name)
            sleep(1)

    def movie(self, name):
        for i in xrange(10):
            print "%s watch movie %s" % (ctime(), name)
            sleep(1)

if "__main__" == __name__:
    entertainment = Entertainment()
    threads = []
    thread1 = threading.Thread(target=entertainment.music, args=("光辉岁月",))
    threads.append(thread1)
    thread2 = threading.Thread(target=entertainment.movie, args=("Avengers",))
    threads.append(thread2)
    for t in threads:
        # t.setDaemon()用于设置守护线程
        # 守护线程如果为True，则主线程不等待子线程结束即结束整个程序
        # 守护线程如果为False，则主线程需要等待子线程结束才结束整个程序

        # t.setDaemon(False)
        t.start()

    for t in threads:
        # t.join()可以等待对应的子线程执行完才继续执行

        t.join()

    print "All threads end!!!"
