#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

S1=list(map(float,inp[0].split(" ")))
S2=list(map(float,inp[1].split(" ")))

def minkowski_diff(S1,S2):
    diffs = []
    for s1 in S1:
        diff = []
        for s2 in S2:
            diff.append(s1-s2)
        diffs.append(diff)
    return diffs

def multiplicity(multiset):
    maxcount = 0
    winner = None
    multi = []
    for line in multiset:
        for x in line:
            multi.append(round(x,4)) # round 4 because of 1/1000 error margin
    current_streak = 1
    multi = sorted(multi)
    for i in range(1,len(multi)):
        if multi[i-1] == multi[i]:
            current_streak+=1
        else:
            current_streak=1
        if current_streak > maxcount:
            maxcount = current_streak
            winner = multi[i]
    return (maxcount,winner)

mdiff = minkowski_diff(S1,S2)
largest_mult, x = multiplicity(mdiff)
print(largest_mult)
print(abs(x))
