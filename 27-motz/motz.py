#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

rna = ''.join(map(str,inp[1:])).replace("\n","")

def is_match(s0,s1):
    if s0 == "A" and s1 == "U": return True
    if s0 == "U" and s1 == "A": return True
    if s0 == "C" and s1 == "G": return True
    if s0 == "G" and s1 == "C": return True
    return False

@memo
def motz(rna):
    n = len(rna)
    if n == 0 or n == 1 : return 1
    m = motz(rna[1:])
    for k in range(1,n):
        if is_match(rna[0],rna[k]):
            m += motz(rna[1:k]) * motz(rna[k+1:])
    return m

print(motz(rna) % 10 ** 6)

# To the difference with Catalan numbers (24-cat.py), not matching
# is taken into account.
