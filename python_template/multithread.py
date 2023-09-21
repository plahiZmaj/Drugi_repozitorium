#! /usr/bin/python2
import time
from threading import Thread
from multiprocessing import Lock
import sys

global thr1running 
thr1running = False

def thr1():
    mx = Lock()
    global thr1running 
    thr1running = True
    num = 1
    numPrev = 1
    while thr1running:
        mx.acquire()
        temp = num 
        num = num + numPrev
        numPrev = temp
        print(num)
        sys.stdout.flush()
        time.sleep(2)
        mx.release()
        time.sleep(0.5)

def thr2():
    while True:
        print("Deamon thread")
        time.sleep(1)


def main():
    global thr1running
    thr1obj = Thread(target=thr1)    #asajnas funkcijo threadu
    thr1obj.start()

    thr2obj = Thread(target=thr2)    #asajnas funkcijo threadu
    thr2obj.setDaemon(True)
    thr2obj.start()

    mx = Lock()
    try:
        while True:
            mx.acquire()
            print("Main thread")
            time.sleep(0.5)
            mx.release()
            time.sleep(3)
    except KeyboardInterrupt:
        try:
            mx.release()
        except Exception as e:
            pass    
        thr1running = False
        print("cakam na thread")
        thr1obj.join()
        print("izhod")        



if __name__ == "__main__":
    main()


