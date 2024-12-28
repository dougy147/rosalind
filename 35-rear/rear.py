#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

couples = []
couple = ()
for l in inp:
    if l == "":
        couples.append(couple)
        couple = ()
    else:
        l = list(map(int,l.split(" ")))
        couple+=(l,)
couples.append(couple)

def flip(s):
    return tuple(reversed(s))

def idea(targets,sources):
    depth = 0
    if targets & sources: return depth
    while True:
        ntargets = set()
        for t in targets:
            for nt in perms(t): ntargets.add(nt)
        nsources = set()
        for s in sources:
            for ns in perms(s): nsources.add(ns)

        if targets & nsources: return depth + 1
        if sources & ntargets: return depth + 1
        if ntargets & nsources : return depth + 2
        depth += 2
        targets = ntargets
        sources = nsources

def perms(source):
    source = tuple(source)
    l = len(source)
    perms = set()
    for i in range(l):
        for j in range(i+1,l):
            left = source[:i]
            center = flip(source[i:j+1])
            right = source[j+1:]
            perms.add(left+center+right)
    return perms

res = []
for target,source in couples:
    #print(target, source)
    res.append(idea({tuple(target)},{tuple(source)}))
print(' '.join(map(str,res)))

# Flipping the target is equivalent (!) to flipping the source
# So, flipping the target to compare it to an already flipped
# source is valid. If it matches then we just have to keep in
# mind that there were 2 permutations (and not one as usual).

# Big thanks:
# https://github.com/zonghui0228/Rosalind-Solutions/blob/master/code/rosalind_rear.py
