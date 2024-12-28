#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

dnas = []
dna = ""
for l in inp:
    if ">" in l:
        if dna != "": dnas.append(dna)
        dna = ""
    else:
        dna+=l
dnas.append(dna)
s,t = dnas
# This is equivalent to computing the Levenshtein's distance

def levenshtein(s,t):
    mat = [[_ for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for r in range(len(mat)):
        mat[r][0] = r
    for r in range(1,len(mat)):
        for c in range(1,len(mat[r])):
            if s[r-1] == t[c-1]:
                mat[r][c] = mat[r-1][c-1]
            else:
                mat[r][c] = min(mat[r-1][c-1],mat[r-1][c],mat[r][c-1]) + 1
    return mat[r][c]

print(levenshtein(s,t))
