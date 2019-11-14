# -*- coding: utf-8 -*-
import random
import threading

class ThreadCrawl(threading.Thread):

    def __init__(self, treadName, age, order ):
        super(ThreadCrawl, self).__init__()
        self.sname = treadName
        self.age = age

    def run(self):
        for i in range(1,10):
            print( "Order " +  str(i) + " Name: " + self.sname + "--"+ " Age: "+ str(self.age) +'--' + str(i))


def main():
    int order =0;
    c_thread = ThreadCrawl("Tread1", random.randint(1,100) )
    c_thread.start()

    c_thread = ThreadCrawl("Tread2", random.randint(1,100) )
    c_thread.start()


if __name__ == '__main__':
    main()