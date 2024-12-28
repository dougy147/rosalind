#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "auto"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

n,m = map(int,inp.split(" "))

res = 0
for k in range(m,n+1):
    res += combinations(k,n)
print(res % 10 ** 6)
