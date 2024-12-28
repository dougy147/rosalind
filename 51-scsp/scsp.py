#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

s,t = inp

def lcs_table(s,t):
    mat = [["" for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for r in range(1,len(s)+1):
        for c in range(1,len(t)+1):
            if s[r-1] == t[c-1]:
                mat[r][c] = mat[r-1][c-1] + s[r-1]
            else:
                mat[r][c] = max(mat[r-1][c],mat[r][c-1],key=len)
    return mat[r][c]

lcs = lcs_table(s,t)
scs = ""
i = 0 # points to s
j = 0 # points to t
k = 0 # points to lcs
while True: # no fear lol
    if k < len(lcs):
        if s[i] == lcs[k] or t[j] == lcs[k]:
            # one or both match with lcs
            if s[i] == lcs[k] and t[j] != lcs[k]:
                while not t[j] == lcs[k]:
                    scs+=t[j]
                    j+=1
            elif t[j] == lcs[k] and s[i] != lcs[k]:
                while not s[i] == lcs[k]:
                    scs+=s[i]
                    i+=1
            scs+=lcs[k]
            k+=1
            i+=1
            j+=1
        else:
            # none matches with lcs
            while not s[i] == lcs[k]:
                scs+=s[i]
                i+=1
            while not t[j] == lcs[k]:
                scs+=t[j]
                j+=1
    else:
        # LCS has already been inserted
        scs+=s[i:]
        scs+=t[j:]
        break
print(scs)
