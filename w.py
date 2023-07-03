#!/usr/bin/python3
f=open("./sqrt2.txt","r")
g=open("./_sqrt2_.txt","w")
g.write(f.read(141))
f.close()
g.close()
