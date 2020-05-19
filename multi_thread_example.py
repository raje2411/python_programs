#!/usr/bin/env python3.7
import threading

def thread_test():
    print("starting thread")
    counter = 0

    while 1 == 1:
        counter = 2
    return

threads = []
for i in range(4):
    t = threading.Thread(target = thread_test)
    threads.append(t)
    t.start()
