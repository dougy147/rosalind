#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

dnas = []
dna = ""
for l in inp:
    if ">" in l:
        if dna != "": dnas.append(dna)
        dna = ""
    else:
        dna+=l
dnas.append(dna)
s,t = dnas

blosum62_mat = [
        ["","A","C","D","E","F","G","H","I","K","L","M","N","P","Q","R","S","T","V","W","Y"],
        ["A",4,0,-2,-1,-2,0,-2,-1,-1,-1,-1,-2,-1,-1,-1,1,0,0,-3,-2],
        ["C",0,9,-3,-4,-2,-3,-3,-1,-3,-1,-1,-3,-3,-3,-3,-1,-1,-1,-2,-2],
        ["D",-2,-3,6,2,-3,-1,-1,-3,-1,-4,-3,1,-1,0,-2,0,-1,-3,-4,-3],
        ["E",-1,-4,2,5,-3,-2,0,-3,1,-3,-2,0,-1,2,0,0,-1,-2,-3,-2],
        ["F",-2,-2,-3,-3,6,-3,-1,0,-3,0,0,-3,-4,-3,-3,-2,-2,-1,1,3],
        ["G",0,-3,-1,-2,-3,6,-2,-4,-2,-4,-3,0,-2,-2,-2,0,-2,-3,-2,-3],
        ["H",-2,-3,-1,0,-1,-2,8,-3,-1,-3,-2,1,-2,0,0,-1,-2,-3,-2,2],
        ["I",-1,-1,-3,-3,0,-4,-3,4,-3,2,1,-3,-3,-3,-3,-2,-1,3,-3,-1],
        ["K",-1,-3,-1,1,-3,-2,-1,-3,5,-2,-1,0,-1,1,2,0,-1,-2,-3,-2],
        ["L",-1,-1,-4,-3,0,-4,-3,2,-2,4,2,-3,-3,-2,-2,-2,-1,1,-2,-1],
        ["M",-1,-1,-3,-2,0,-3,-2,1,-1,2,5,-2,-2,0,-1,-1,-1,1,-1,-1],
        ["N",-2,-3,1,0,-3,0,1,-3,0,-3,-2,6,-2,0,0,1,0,-3,-4,-2],
        ["P",-1,-3,-1,-1,-4,-2,-2,-3,-1,-3,-2,-2,7,-1,-2,-1,-1,-2,-4,-3],
        ["Q",-1,-3,0,2,-3,-2,0,-3,1,-2,0,0,-1,5,1,0,-1,-2,-2,-1],
        ["R",-1,-3,-2,0,-3,-2,0,-3,2,-2,-1,0,-2,1,5,-1,-1,-3,-3,-2],
        ["S",1,-1,0,0,-2,0,-1,-2,0,-2,-1,1,-1,0,-1,4,1,-2,-3,-2],
        ["T",0,-1,-1,-1,-2,-2,-2,-1,-1,-1,-1,0,-1,-1,-1,1,5,0,-2,-2],
        ["V",0,-1,-3,-2,-1,-3,-3,3,-2,1,1,-3,-2,-2,-3,-2,0,4,-3,-1],
        ["W",-3,-2,-4,-3,1,-2,-2,-3,-3,-2,-1,-4,-4,-2,-3,-3,-2,-3,11,2],
        ["Y",-2,-2,-3,-2,3,-3,2,-1,-2,-1,-1,-2,-3,-1,-2,-2,-2,-1,2,7]
    ]

def needleman_wunsch(s,t):
    linear_gap_penalty = 5
    mat = [[-linear_gap_penalty for _ in range(len(t)+1)] for _ in range(len(s)+1)]
    for r in range(len(mat)):
        mat[r][0] = -linear_gap_penalty
    mat[0][0] = 0

    for r in range(1,len(mat)):
        for c in range(1,len(mat[r])):
            mat[r][c] = max(mat[r-1][c-1] + blosum62[(s[r-1],t[c-1])],
                            max([mat[nr][c] for nr in range(1,r+1)]) - linear_gap_penalty,
                            max([mat[r][nc] for nc in range(1,c+1)]) - linear_gap_penalty,
                            )

    max_alignment_score = mat[r][c]
    return max_alignment_score

# Build dictionnary from original BLOSUM62 matrix
blosum62 = {}
for r in range(1,len(blosum62_mat)):
    for c in range(1,len(blosum62_mat[0])):
        blosum62[(blosum62_mat[0][c],blosum62_mat[r][0])] = blosum62_mat[r][c]

max_alignment_score = needleman_wunsch(s,t) # max score
print(max_alignment_score)

# https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm
