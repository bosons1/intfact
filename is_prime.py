#!/usr/bin/python3
import sys

def decide(num, magic, p):
    fp = ""
    if p == 0:
        fp = open("./pi.txt","r")
    else:
        fp = open("./sqrt2.txt", "r")
    fp.read(2)
    ctr = 0
    l = len(num)
    pos = 0
    while True:
        pp = str(fp.read(1))
        if not pp or pp == "" or len(pp) == 0:
            print("Out of precision Error!!")
            sys.exit(3)
        pos = pos + 1
        n = num[ctr % l]
        if pp == n:
            ctr = ctr + 1
            if ctr == magic*l:
                break
    fp.close()
    return pos

def primality_test(num):
    m = open("zeros2.txt","r")
    line = m.readline()
    magic = int(line.rstrip())
    d1 = decide(num, magic, 0)
    d2 = decide(num, magic, 1)
    initial_truth_value = False
    if d1 < d2:
        initial_truth_value = 0
    elif d1 == d2:
        initial_truth_value = 2
    elif d1 > d2:
        initial_truth_value = 1
    line = ""
    while True:
        line = m.readline()
        if not line or line == "" or len(line) == 0:
            print("Out of Zeros")
            sys.exit(4)
        magic = int(line.rstrip())
        d1 = decide(num, magic, 0)
        d2 = decide(num, magic, 1)
        truth_value = False
        if d1 < d2:
            truth_value = 0
        elif d1 == d2:
            truth_value = 2
        elif d1 > d2:
            truth_value = 1
        if truth_value != initial_truth_value:
            print([d1, d2])
            if d1 == d2 and d1 % 2 == 1:
                m.close()
                return True
            elif d1 == d2 and d1 % 2 == 0:
                m.close()
                return False
            elif abs(d1-d2) == 1:
                m.close()
                return False
            initial_truth_value = truth_value
    m.close()
    return None

num = str(sys.argv[1])
rnum = num[::-1]
is_prime = primality_test(rnum)
if is_prime:
    print(num + " is a Prime Number")
else:
    print(num + " is a Composite Number")
