#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "auto"
from rosalind_helper import *

cached={}
def memo(f):
    global cached
    def m(*x):
        if not str([*x]) in cached: cached[str([*x])] = f(*x)
        return cached[str([*x])]
    return m

@memo
def rfib(n,a,d): # a = adult at, d = dead at
    if n == 1 or n <= a: return 1
    elif a < n and n <= d: return rfib(n-1,a,d) + rfib(n-a,a,d)
    elif n == d + 1: return rfib(n-1,a,d) + rfib(n-a,a,d) - 1
    elif n >= d + 2: return rfib(n-1,a,d) + rfib(n-a,a,d) - rfib(n-d-1,a,d)

gen,life=map(int,inp.split(" "))
fertile = 2
res = rfib(gen,fertile,life)
print(f"{res}")

# https://arxiv.org/pdf/2312.13098
