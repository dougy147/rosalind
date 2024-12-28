#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

dna = ''.join(map(str,inp[1:]))

def pseudo_kmp(s):
    n = len(s)
    failure_array = [0 for _ in range(n)]
    l = 0
    for k in range(1,n):
        #if k % 100 == 0: print(f"{k} on {n}")
        max_len = 0
        for j in range(1,n-k+1):
            sub    = s[j:j+k]
            prefix = s[:k]
            if sub == prefix:
                #if len(prefix) > max_len: max_len = len(prefix)
                failure_array[k+j-1] = len(prefix)
                l = len(prefix)
        if l < len(prefix): break

    return failure_array

failure_array = pseudo_kmp(dna)
print(" ".join(map(str,failure_array)))

# See here for "true" KMP algo
# http://youtu.be/watch?v=pu2aO_3R118

# Cheers to zonghui0228 for the last pieces of "understanding":
# https://github.com/zonghui0228/Rosalind-Solutions/blob/master/code/rosalind_kmp.py
