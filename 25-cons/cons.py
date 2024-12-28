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
        if not dna == "": dnas.append(dna)
        dna = ""
    else: dna+=l.replace("\n","")
dnas.append(dna)

def profile_matrix(dnas):
    rows = len(dnas)
    cols = len(dnas[0])

    matrix = [[_ for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            matrix[r][c] = dnas[r][c]

    profile_matrix = [[_ for _ in range(cols+1)] for _ in range(4)]
    for c in range(cols):
        profile = {"A":0,"C":0,"G":0,"T":0}
        for r in range(rows):
            profile[matrix[r][c]]+=1
        for i,k in enumerate(profile):
            profile_matrix[i][0] = k + ":"
            profile_matrix[i][c+1] = profile[k]

    consensus = [0 for x in range(cols)]
    consensus_string = ["" for x in range(cols)]
    for c in range(1,cols+1):
        for r in range(4):
            if profile_matrix[r][c] > consensus[c-1]:
                consensus[c-1] = profile_matrix[r][c]
                consensus_string[c-1] = profile_matrix[r][0].replace(":","")
    print(''.join(map(str,consensus_string)))

    for _ in profile_matrix:
        print(' '.join(map(str,_)))

profile_matrix(dnas)
