#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

dnas, dna = [], ""
for l in inp:
    if ">" in l:
        if dna != "": dnas.append(dna)
        dna = ""
    else: dna+=l
dnas.append(dna)

def p_distance(s1,s2):
    assert len(s1) == len(s2)
    c = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]: c+=1
    return c / len(s1)

mat = []
for dna1 in dnas:
    tmp = [-1 for _ in range(len(dnas))]
    for i in range(len(dnas)):
        dna2 = dnas[i]
        tmp[i] = p_distance(dna1,dna2)
    mat.append(tmp)

for row in mat:
    print(' '.join(map(str,row)))
