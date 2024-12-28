#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "auto"
from rosalind_helper import *

# https://aliquote.org/post/rosalind-independent-alleles/
k, N = map(int,inp.split(" "))

def factorial(n):
    m=1
    while n > 0:
        m*=n
        n-=1
    return m

def C(k,n):
    return factorial(n) / (factorial(n-k) * factorial(k))

def proba(k,N):
    p = 0
    for n in range(N):
        # important: compute number of combinations/permutations of n among 2**k
        c = C(n,2**k) # combinations
             # p(AaBb)     p(NOT AaBb)
        p += c * ((1/4)**n) * ((3/4)**(2**k-n))
    return 1-p

print(proba(k,N))
