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
    else: dna+=l
dnas.append(dna)

def overlap(s1,s2):
    if len(s1) % 2 != 0:
        l1 = len(s1) // 2 + 1 + 1
    else:
        l1 = len(s1) // 2 + 1
    if len(s2) % 2 != 0:
        l2 = len(s2) // 2 + 1 + 1
    else:
        l2 = len(s2) // 2 + 1

    left_s1  = s1[:l1]
    right_s1 = s1[l1-1-1:]

    left_s2  = s2[:l2]
    right_s2 = s2[l2-1-1:]

    if left_s1 in s2 or right_s1 in s2 or left_s2 in s1 or right_s2 in s1:
        # which direction? (lazy mode)
        match1 = ""
        s1s2 = ""
        i = 1
        while s2[:i] in s1:
            match1=s2[:i]
            i+=1

        match2 = ""
        s2s1 = ""
        i = 1
        while s1[:i] in s2:
            match2=s1[:i]
            i+=1

        len_match = max(len(match1),len(match2))
        if len_match < l1 and len_match < l2:
            return (False, -1, "")

        if len(match1) > len(match2):
            # s1->s2
            match = match1
            m = s1 + s2[len(match):]
        else:
            # s2->s1
            match = match2
            m = s2 + s1[len(match):]
        return (True,len_match,m)

    else:
        return (False, -1, "")

q = dnas
s1 = q.pop(0)

while q != []:
    longest_overlap = 0
    idx_longest_overlap = float("Inf")
    concat = ""
    for i in range(len(q)):
        s2 = q[i]
        ok, overlap_size, s3 = overlap(s1,s2)
        if not ok: continue
        if overlap_size > longest_overlap:
            longest_overlap = overlap_size
            idx_longest_overlap = i
            concat = s3
    assert concat != ""
    q.pop(idx_longest_overlap)
    s1 = concat

chromosome = s1
print(chromosome)

# This took me some time to implement the overlap function.
# I thought it would be inefficient for the required input.
# Guess more algo/complexity/whatever training is needed...
