#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

n = int(inp[0])
raw_sets = inp[1:]
excluded = ["{",","," ","}"]
sets = []
for rs in raw_sets:
    s = set()
    rs = rs.split(" ")
    for x in rs:
        x = x.replace(",","").replace("{","").replace("}","")
        s.add(int(x))
    sets.append(s)

A,B = sets
full_set = set([x for x in range(1,n+1)])

print(A | B) # union
print(A & B) # intersection
print(A - B) # A - B
print(B - A) # B - A
print(full_set - A) # Ac (c=complement)
print(full_set - B) # Bc
