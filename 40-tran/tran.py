#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

dnas = []
dna=""
for l in inp:
    if ">" in l:
        if dna != "": dnas.append(dna)
        dna = ""
    else:
        dna+=l
dnas.append(dna)

s1, s2 = dnas
assert len(s1) == len(s2)

def transition_transversion_ratio(s1,s2):
    transitions = 0
    transvertions = 0
    for i in range(len(s1)):
        a = s1[i]
        b = s2[i]
        if a != b:
            if (a=="A" and b=="G") or (a =="G" and b=="A"): transitions+=1
            elif (a=="C" and b=="T") or (a =="T" and b=="C"): transitions+=1
            else: transvertions+=1

    return transitions / transvertions

print(transition_transversion_ratio(s1,s2))
