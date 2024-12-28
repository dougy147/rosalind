#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

n = int(inp[0])

adjencies = {}
for adjs in inp[1:]:
    n1, n2 = map(int,adjs.split(" "))
    if n1 in adjencies: adjencies[n1].append(n2)
    else: adjencies[n1] = [n2]
    if n2 in adjencies: adjencies[n2].append(n1)
    else: adjencies[n2] = [n1]

subtrees = []
for k in adjencies:
    t0 = [k]
    t1 = adjencies[k]
    found = False
    for t in subtrees :
        cur = []
        for u in t0 + t1:
            if u in t:
                found = True
                subtrees[subtrees.index(t)] = list(set(t0+t1+subtrees[subtrees.index(t)]))
                break
        if found: break
    if not found:
        subtrees.append(t0+t1)

nodes = set()
for t in subtrees:
    for st in t:
        nodes.add(st)

for i in range(len(subtrees)):
    for j in range(len(subtrees)):
        if i == j: break
        if len(subtrees[i]) + len(subtrees[j]) > len(set(subtrees[j]+subtrees[i])):
            subtrees[i] = list(set(subtrees[j]+subtrees[i]))
            subtrees[j] = []

subtrees = [x for x in subtrees if x != []]

missing_nodes = n - len(nodes)    # each missing = 1 edge missing
unconnected_trees = len(subtrees)
print(missing_nodes + unconnected_trees - 1)
