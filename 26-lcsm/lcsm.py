#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

ids = []
dnas = []
dna = ""
for l in inp:
    if ">" in l:
        ids.append(l)
        if dna != "": dnas.append(dna)
        dna = ""
    else:
        dna+=l.replace("\n","")
dnas.append(dna)

def get_substrings(string):
    subs = []
    # from longest to shortest
    for i in range(len(string)):
        for j in range(len(string)):
            s = string[j:len(string)-i]
            if s == "": continue
            subs.append(s)
    return sorted(subs,key=len,reverse=True)

for sub in get_substrings(dnas[0]):
    match = True
    for dna in dnas[1:]:
        if not sub in dna:
            match = False
            break
    if match:
        print(sub)
        break
