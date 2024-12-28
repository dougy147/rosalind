#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

trees = []
pairs = [] # pairs for which to compute distance in the tree

for l in inp:
    if ";" in l: trees.append(l)
    elif not l == "": pairs.append(tuple(l.split(" ")))

def distance(pair,tree):
    a,b=pair
    index_a = tree.index(a)
    index_b = tree.index(b)
    piece_of = tree[min(index_a,index_b):max(index_a,index_b)]
    piece_of = ''.join(map(str,[x for x in piece_of if x in ["(",",",")"]]))
    nestedness = 0
    for elem in piece_of:
        if elem == "(": nestedness+=1
        if elem == ")": nestedness-=1
    nestedness = abs(nestedness)
    if piece_of == "": return 2
    if piece_of.replace(",","") == "": return 2
    if piece_of.replace("(","") == "": return len(piece_of)
    if piece_of.replace(")","") == "": return len(piece_of)
    if not "(" in piece_of:
        print(piece_of)
        if piece_of[-1] == "," and piece_of[0] == ")":
            return piece_of.count(")") + 2
        elif piece_of[-1] == "," or piece_of[0] == ")":
            return piece_of.count(")") + 2
        else:
            return piece_of.count(")") + 1
    if not ")" in piece_of:
        if piece_of[0] == "," and piece_of[-1] == "(":
            return piece_of.count("(") + 2
        elif piece_of[0] == "," or piece_of[-1] == "(":
            return piece_of.count("(") + 2
        else:
            return piece_of.count("(") + 1
    while ",," in piece_of:
        piece_of = piece_of.replace(",,",",")
    while "(,)" in piece_of:
        piece_of = piece_of.replace("(,)","")
    return piece_of.count(")") + piece_of.count("(") + 2

distances = []
for i in range(len(trees)):
    tree = trees[i]
    pair = pairs[i]
    d = distance(pair,tree)
    #print(f"\"{pair[0]}\" and \"{pair[1]}\" have distance={d} in tree=\"{tree}\"")
    distances.append(d)

print(' '.join(map(str,distances)))

# https://en.wikipedia.org/wiki/Newick_format
