# -*- coding: utf-8 -*-

import threading

class ThreadCrawl(threading.Thread):

    def __init__(self, name):
        super(ThreadCrawl, self).__init__()
        self.sname = name

    def run(self):
        for i in range(1,10):
            print( self.sname + "--"+ str(i))


def main():
    c_thread = ThreadCrawl("Tread1")
    c_thread.start()

    c_thread = ThreadCrawl("Tread2")
    c_thread.start()


main()