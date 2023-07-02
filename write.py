#!/usr/bin/python3
import sys
f=open("./zeros6","r")
g=open("./zeros2.txt","w")
g.write("10\n")
lines=f.readlines()
for line in lines:
    l = line.lstrip().rstrip()
    i = l.index(".")
    l = l[:i]
    g.write(l)
    g.write("\n")
g.close()
f.close()
