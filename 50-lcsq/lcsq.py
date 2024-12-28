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
        if dna!="":dnas.append(dna)
        dna=""
    else: dna+=l
dnas.append(dna)
s,t = dnas

# https://en.wikipedia.org/wiki/Longest_common_subsequence

def lcs_table(s,t):
    mat = [["" for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for r in range(1,len(s)+1):
        for c in range(1,len(t)+1):
            if s[r-1] == t[c-1]:
                mat[r][c] = mat[r-1][c-1] + s[r-1]
            else:
                mat[r][c] = max(mat[r-1][c],mat[r][c-1],key=len)
    return mat[r][c]

print(lcs_table(s,t))

# How not to see the similarity with the Levenshtein distance!
# Solving in O(len(s)*len(t))
