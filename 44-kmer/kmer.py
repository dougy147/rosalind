#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

dna = ''.join(map(str,inp[1:]))

def k_mer_composition(k,depth=0,current=[],compo=None):
    if compo == None: compo = []
    if depth == k:
        compo.append(current)
        return
    for b in ["A","C","G","T"]:
        k_mer_composition(k,depth+1,current+[b],compo)
    return compo

def k_mer(s,k):
    k_mers = {}
    for km in k_mer_composition(4):
        k_mers[tuple(km)] = 0
    for i in range(len(s)-k+1): # do not forget +1 lol
        k_mers[tuple(s[i:i+k])] += 1
    return k_mers

print(' '.join(map(str,k_mer(dna,k=4).values())))
