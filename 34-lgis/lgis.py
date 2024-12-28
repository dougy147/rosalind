#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

n = int(inp[0])
pi_perm = list(map(int,''.join(map(str,inp[1:])).split(" ")))
assert(len(pi_perm) == n)

def longest_inc(lst):
    cands = [[lst[0]]]
    for i in range(1,len(lst)):
        elem = lst[i]
        inserted = False
        for c in sorted(cands,key=len,reverse=True):
            # insert in candidates
            if elem > c[-1]:
                inserted = True
                cand = c + [elem]
                cands.append(cand)
                break
        # remove if same length but higher ending value
        if not inserted:
            cand = [elem]
            cands.append(cand)
        for c in list(filter(lambda x: len(x) == len(cand),cands)):
            if c == cand: continue
            if c[-1] > cand[-1]: cands.pop(cands.index(c))
            else: cands.pop(cands.index(cand))
            break
    return max(cands,key=len)

def longest_dec(lst):
    cands = [[lst[0]]]
    for i in range(1,len(lst)):
        elem = lst[i]
        inserted = False
        for c in sorted(cands,key=len,reverse=True):
            # insert in candidates
            if elem < c[-1]:
                inserted = True
                cand = c + [elem]
                cands.append(cand)
                break
        # remove if same length but higher ending value
        if not inserted:
            cand = [elem]
            cands.append(cand)
        for c in list(filter(lambda x: len(x) == len(cand),cands)):
            if c == cand: continue
            if c[-1] < cand[-1]: cands.pop(cands.index(c))
            else: cands.pop(cands.index(cand))
            break
    return max(cands,key=len)

inc = longest_inc(pi_perm)
dec = longest_dec(pi_perm)

print(' '.join(map(str,inc)))
print(' '.join(map(str,dec)))

# https://youtu.be/watch?v=OIU8ZLC4qIQ
