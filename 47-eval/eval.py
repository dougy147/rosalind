#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

n,dna,A = inp
n = int(n)
A = list(map(float,A.split(" "))) # contains GC content

def proba(dna,gc_content):
    # probability to generate exactly "dna"
    # given GC content
    g_or_c = gc_content/2
    a_or_t = (1-gc_content)/2
    p = 1
    for b in dna:
        if b == "A" or b =="T": p*=a_or_t
        elif b == "G" or b =="C": p*=g_or_c
        else: raise error
    return p

B = []
for gc in A:
    p_dna = proba(dna,gc)
    #print(p_dna) # p to generate exactly dna, given GC, when length of dna = len(dna)
    p = 0
    for x in range(n-len(dna)+1):
        p += p_dna
    B.append(p)
print(' '.join(map(str,B)))
