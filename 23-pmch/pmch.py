#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

# Hard time getting it because of:
#    - own brain
#    - dubious explainations on Rosalind.
# https://jangbearbio.tistory.com/m/43

rna = ''.join(map(str,inp[1:])).replace("\n","")
A,G,U,C = rna.count("A"),rna.count("G"),rna.count("U"),rna.count("C")

AU, GC = sorted([A,U]), sorted([G,C])

# We need to divide by number of permutations of (length / 2) elements.
def factorial(n):
    m=1
    while n > 0:
        m*=n
        n-=1
    return m

def A(k,n):
    return factorial(n) // factorial(n-k)

print(A(AU[0],AU[1]) * (A(GC[0],GC[1])))
