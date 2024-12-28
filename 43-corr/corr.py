#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

genome_substrings = []
g = ""
for l in inp:
    if ">" in l:
        if not g == "": genome_substrings.append(g)
        g = ""
    else:
        g+=l
genome_substrings.append(g)

def reverse_complement(s):
    r = ""
    for b in s:
        match b:
            case "A": r+="T"
            case "T": r+="A"
            case "G": r+="C"
            case "C": r+="G"
    return ''.join(map(str,reversed(r)))

def is_correct(s1,dataset):
    c = 0
    for s2 in dataset:
        if s1 == s2 or s1 == reverse_complement(s2):
            c+=1
        if c >= 2: return True
    return False

def hamm_distance(s,t):
    hamm = 0
    for i in range(len(s)):
        if s[i] != t[i]: hamm+=1
    return hamm

def apply_correction(s1,dataset,incorrects):
    for s2 in dataset:
        if s1 == s2: continue
        if s2 in incorrects: continue
        if hamm_distance(s1,s2) == 1:
            return s2
        rev1 = reverse_complement(s1)
        if hamm_distance(rev1,s2) == 1:
            return reverse_complement(s2)
        rev2 = reverse_complement(s2)
        if hamm_distance(s1,rev2) == 1:
            return rev2

incorrects = []
for s in genome_substrings:
    if not is_correct(s,genome_substrings):
        incorrects.append(s)

for s in incorrects:
    corrected = apply_correction(s,genome_substrings,incorrects)
    print(f"{s}->{corrected}")
