#! /usr/bin/python2
import time
from copy import copy, deepcopy


def main():
    spisek1 = ["miska1", "miska2", "miska3"]
    spisek2 = spisek1
    
    temp = spisek1.pop(1)
    print(temp)

    spisek1.append(temp)

    print("spisek 1 po append: " + repr(spisek1))

    spisek3 = copy(spisek1)
    spisek3.pop(1)
    print(repr(spisek1))
    print(repr(spisek3))

if __name__ == "__main__":
    main()