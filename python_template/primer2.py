#! /usr/bin/python2
import time
from copy import copy, deepcopy


class Kvader():
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def ploscina(self):
        return self.a * self.b
    


class Kvadrat(Kvader, object):
    def __init__(self, a):
        super(Kvadrat,self).__init__(a, a)

def main():
  kvadric = Kvader(1.0, 3.0)
  kvadratic = Kvadrat(2.0)
  print(kvadric.ploscina()) 
  print(kvadratic.ploscina())  
     

if __name__ == "__main__":
    main()