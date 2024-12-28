#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "auto"
from rosalind_helper import *

n,k = map(int,inp.split(" "))

def factorial(n):
    m=1
    while n > 0:
        m*=n
        n-=1
    return m

def A(k,n): # arrangement because order matters
    return int(factorial(n) / factorial(n-k))

print(A(k,n) % 1_000_000)
