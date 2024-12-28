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

def lcs_table(s,t):
    mat = [["" for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for r in range(1,len(s)+1):
        for c in range(1,len(t)+1):
            if s[r-1] == t[c-1]:
                mat[r][c] = mat[r-1][c-1] + s[r-1]
            else:
                mat[r][c] = max(mat[r-1][c],mat[r][c-1],key=len)
    return mat[r][c]

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

def levenshtein_align(s,t):
    new_s = ""
    new_t = ""
    mat = [[_ for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for r in range(len(mat)):
        mat[r][0] = r
    for r in range(1,len(mat)):
        for c in range(1,len(mat[r])):
            if s[r-1] == t[c-1]:
                mat[r][c] = mat[r-1][c-1]
            else:
                mat[r][c] = min(mat[r-1][c-1],mat[r-1][c],mat[r][c-1]) + 1
    # now check path in reverse from last cell
    r,c = len(mat)-1, len(mat[0])-1
    queue = [(r,c)]
    while (r >= 0 and c >= 0):
        if r == 0 and c == 0: break
        minimum = min(mat[r-1][c-1],mat[r-1][c],mat[r][c-1])
        if minimum == mat[r-1][c-1]: # either same, or substitution
            new_s = s[r-1] + new_s
            new_t = t[c-1] + new_t
            r-=1
            c-=1
        elif minimum == mat[r-1][c]: # insertion of s
            new_s = s[r-1] + new_s
            new_t = "-" + new_t
            r-=1
        elif minimum == mat[r][c-1]: # insertion of t
            new_s = "-" + new_s
            new_t = t[c-1] + new_t
            c-=1
    return (new_s,new_t)

print(levenshtein(s,t))
ns, nt = levenshtein_align(s,t)
print(ns)
print(nt)
