#! /usr/bin/python2
import time


i = 3
global n 
n = 2


def main():
    global n
    print(str(n))
    print("To je moje sporocilo: %f" % n)
    i = 2
    print("Hello World!")
    


if __name__ == "__main__":
    main()





