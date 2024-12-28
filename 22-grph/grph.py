#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

ids = []
dna = []

current_dna = ""
started = False
for x in inp:
    if ">" in x:
        ids.append(x.replace("\n",""))
        if started:
            dna.append(current_dna)
            current_dna = ""
        else: started = True
    else: current_dna+=x.replace("\n","")
dna.append(current_dna)

def overlap(a,b):
    if b[:3] == a[-3:]: return True
    return False

for i in range(len(dna)):
    for j in range(i+1,len(dna)):
        dna1 = dna[i]
        dna2 = dna[j]
        if overlap(dna1,dna2):
            print(ids[i].replace(">",""),ids[j].replace(">",""))
        if overlap(dna2,dna1):
            print(ids[j].replace(">",""),ids[i].replace(">",""))
