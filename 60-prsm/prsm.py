#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

n = int(inp[0])
proteins = []
R = []
for elem in inp[1:]:
    if "." in elem: R.append(float(elem))
    else: proteins.append(elem)

mono = { "A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259, "F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406, "K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293, "P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203, "T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333 }

def minkowski_diff(S1,S2):
    diffs = []
    for s1 in S1:
        for s2 in S2:
            diffs.append(round(s1-s2,4)) # rounding with error margin
    return diffs

def multiplicity(multiset):
    multi = sorted(multiset)
    max_streak = 0
    current_streak = 1
    for i in range(1,len(multi)):
        if multi[i-1] == multi[i]:
            current_streak+=1
            if current_streak >= max_streak:
                max_streak = current_streak
        else:
            current_streak = 1
    return max_streak

def weight(S):
    return sum([mono[s] for s in S])

def complete_spectrum(S):
    spectrum = []
    for i in range(1,len(S)):
        pref = S[:i]
        suff = S[i:]
        spectrum.append(weight(pref))
        spectrum.append(weight(suff))
    spectrum.append(weight(S))
    return spectrum

max_mult = 0
winner = ""
for prot in proteins:
    S = []
    for mass in complete_spectrum(prot):
        S.append(mass)
    mdiff = minkowski_diff(R,S)
    mult = multiplicity(mdiff)
    if mult > max_mult:
        max_mult = mult
        winner = prot
print(max_mult)
print(winner)
