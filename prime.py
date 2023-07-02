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

num=str(sys.argv[1])
m = open("zeros2.txt","r")
line = m.readline()
magic = int(line.rstrip())
print(magic)
d1 = decide(num, magic, 0)
d2 = decide(num, magic, 1)
initial_truth_value = False
if d1 < d2:
    initial_truth_value = True
zero_index = 0
print(d1, d2, zero_index)
line = ""
while True:
    line = m.readline()
    if not line or line == "" or len(line) == 0:
        print("Out of Zeros")
        sys.exit(4)
    magic = int(line.rstrip())
    print(magic)
    d1 = decide(num, magic, 0)
    d2 = decide(num, magic, 1)
    truth_value = False
    if d1 < d2:
        truth_value = True
    if truth_value != initial_truth_value:
        print(d1, d2, zero_index, line)
        break
    zero_index = zero_index + 1
    print(d1, d2, zero_index)
m.close()
