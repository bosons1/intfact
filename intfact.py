#!/usr/bin/python3
import sys
from mpmath import *
from gmpy2 import *

def satisfies(degree, digit):
    f=open("./pi.txt", "r")
    g=open("./sqrt2.txt","r")
    c = 0
    f.read(2)
    g.read(2)
    pp = ""
    tt = ""
    while True:
        pp = str(f.read(1))
        tt = str(g.read(1))
        if pp == str(digit):
            c = c + 1
            if c == degree:
                break
    f.close()
    g.close()
    d = int(pp) + int(tt)
    if d == 1 or d == 11:
        return True
    else:
        return False

def divides(num, factor):
    fz = mpz(str(factor))
    nz = mpz(num)
    if fz <= 1:
        return False, ""
    rz = fmod(nz, fz)
    if rz == 0:
        qz = fdiv(nz, fz)
        return True, str(qz)
    else:
        return False, ""

num=str(sys.argv[1])
l = len(num)
bin_factor = ""
zero_index = 1
mp.prec=27
mp.dps=27
i = 0
while True:
   zero = str(zetazero(zero_index).imag)
   idx = zero.index(".")
   zero = zero[idx + 1:]
   zero = zero[:8]
   nn = num[l - 1 - i]
   i = (i + 1) % l
   hit = False
   nzeros = 0
   zero_index = zero_index + 1
   for digit in zero:
       if digit == '0':
           digit = 10
       if satisfies(int(digit), int(nn)) == True:
           hit = True
           break
   nzeros = nzeros + zero.count("0")
   if hit == True:
       bin_factor = bin_factor + bin(nzeros)[2:]
       nzeros = 0
       dec_factor = int(bin_factor[::-1],2)
       success, other_factor = divides(num, dec_factor)
       if success == 1 and i == 0:
           print(num + " = " + str(dec_factor) + " X " + str(other_factor))
           break
       elif success == 2:
           print(num + " is a Prime Number or *not* a Semi-Prime but Composite.")
