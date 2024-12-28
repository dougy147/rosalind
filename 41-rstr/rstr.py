#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

N,x = map(float,inp[0].split(" "))
s = ''.join(map(str,inp[1:]))

gc = x
at = 1 - x

a = at/2
t = at/2
g = gc/2
c = gc/2

p = lambda x: a if (x=="A" or x=="T") else g
ps = [p(x) for x in s]
p = 1
for x in ps:
    p*=x

p_none = (1-p) ** N # proba that there is no string like s
print(1-p_none)
