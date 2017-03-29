# -*- coding:utf-8 -*-

# single process single thread (Spst)

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
    entertainment.music("光辉岁月")
    entertainment.movie("Avengers")
