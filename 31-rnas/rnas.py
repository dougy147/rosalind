#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

rna = ''.join(map(str,inp[0:])).replace("\n","")

def is_match(s0,s1):
    if s0 == "A" and s1 == "U": return True
    if s0 == "U" and s1 == "A": return True
    if s0 == "C" and s1 == "G": return True
    if s0 == "G" and s1 == "C": return True

    if s0 == "U" and s1 == "G": return True
    if s0 == "G" and s1 == "U": return True
    return False

@memo
def wobble(rna):
    n = len(rna)
    if n == 0 or n == 1 : return 1
    m = wobble(rna[1:])
    for k in range(1,n):
        if k >= 4 and is_match(rna[0],rna[k]):
            m += wobble(rna[1:k]) * wobble(rna[k+1:])
    return m

print(wobble(rna))
