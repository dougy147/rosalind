#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

rna = ''.join(map(str,inp[1:])).replace("\n","")

@memo
def catalan(circle):
    l = len(circle)
    if l == 0 or l == 1: return 1

    cn = 0
    for k in range(1,l,2):
        U,A,G,C = circle.count("U"),circle.count("A"),circle.count("G"),circle.count("C")
        if U == A and G == C:
            cn += catalan(circle[1:k]) * catalan(circle[k+1:])

    return cn % 10**6

print(catalan(rna))
