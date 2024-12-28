#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "auto"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

n = int(inp)

import math

def common_log(n):
    return math.log(n,10)


def proba(k):
    # proba that two diploids share AT LEAST k
    # of their n chromosomes each
    p = combinations(k,2*n) * (0.25 ** k) * (0.25 ** (n-k))
    return p

A = [0 for k in range(2*n)]
p = 0
for k in reversed(range(1,2*n+1)):
    p += proba(k)
    c = common_log(p)
    A[k-1] = c
print(' '.join(map(str,A)))

# For this problem, one needs to understand what is a diploid.
# A diploid is a couple of homologuous chromosomes.
# Each chromosome has "n" genes (made of DNA and/or proteins).
# So, a diploid has 2n genes, because it has two chromosomes.
#
# The question is: if you have TWO (!) diploids, what is the
# common logarithm of the probability for them to have k genes
# in common, with k=1 to k=2*n.
#
# At first I thought there was only a single diploid, with
# only two chromosomes.
