#!/usr/bin/python3
import sys
MAGIC=10

def factorize(num, p):
    global MAGIC
    fp = ""
    fe = ""
    factor = ""
    if p == 0:
         fp = open("./pi.txt","r")
         fe = open("./sqrt2.txt","r")
    else:
         fp = open("./sqrt2.txt","r")
         fe = open("./e.txt","r")
    fp.read(2)
    fe.read(2)
    ctr = 0
    l = len(num)
    p_vec = []
    e_vec = []
    pos = 0
    p_string = ""
    while True:
        pp = str(fp.read(1))
        p_string = p_string + pp
        pos = pos + 1
        n = num[ctr % l]
        if pp == n:
            p_vec.append(pos)
            ctr = ctr + 1
            if ctr == MAGIC*l:
                break
        else:
            p_vec.append(0)
    e_string = str(fe.read(pos))[::-1]
    ctr = 0
    pos2 = 0
    while True:
        ee = str(e_string[pos2])
        n = num[ctr % l]
        if ee == n:
            ctr = ctr + 1
            if p_vec[pos2] == 1:
                if ee == p_string[pos2]:
                    factor = factor + "1"
                else:
                    zero_index1 = pos2 + 1
                    zero_index2 = pos
                    input([zero_index1, zero_index2])
        pos = pos - 1
        if pos == len(e_string):
            break
    fp.close()
    fe.close()
    return factor

num=str(sys.argv[1])
factor1 = factorize(num, 0)[::-1]
factor2 = factorize(num, 1)
dec1 = int(factor1, 2)
dec2 = int(factor2, 2)
if dec1*dec2 == int(num):
    print(num + " = " + str(dec1) + " X " + str(dec2))
else:
    print(num + " is a prime number.")
