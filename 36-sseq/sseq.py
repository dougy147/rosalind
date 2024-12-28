#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

parsed_first = False
dnas = []
dna = ""
c = 0
for l in inp:
    if ">" in l:
        if c > 0: parsed_first = True
        if parsed_first and dna != "":
            dnas.append(dna)
            dna = ""
        c+=1
        continue
    else:
        if not parsed_first: dna+=l
        else: dna+=l
dnas.append(dna)

s,t = dnas

def get_indices(s,t,sindex=0,current = [],indices=None):
    if indices == None: indices = []
    if len(s) < len(t): return

    if t == "":
        print(' '.join(map(str,current)))
        indices.append(current)
        exit() # only one is needed
        return

    for i in range(1,len(s)-1):
        if s[i-1] == t[0]:
            get_indices(s[i:],t[1:],sindex+i,current + [sindex + i],indices)

    return indices

print(get_indices(s,t))
