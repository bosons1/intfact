#!/usr/bin/python3
import sys
MAGIC=10

def factorize(num, p):
    global MAGIC
    fp = open("./pi.txt","r")
    fp.read(2)
    ctr = 0
    l = len(num)
    pos = 0
    while True:
        pp = str(fp.read(1))
        pos = pos + 1
        n = num[ctr % l]
        if pp == n:
            ctr = ctr + 1
            if ctr == MAGIC*l:
                break
    print(pos)
    fp.close()

num=str(sys.argv[1])
