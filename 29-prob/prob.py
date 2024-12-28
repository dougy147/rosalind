#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

dna = inp[0]
A = list(map(float,inp[1].split(" ")))

import math
def common_log(x):
    return math.log(x,10)

def freqs_given_gc(gc_content):
    freqs = {"A": (1 - gc_content) / 2, "T": (1 - gc_content) / 2, "G": gc_content / 2, "C": gc_content / 2}
    return freqs

common_logs = []
for gc in A:
    freqs = freqs_given_gc(gc)
    p = 1 # proba of build current dna string with THAT gc
    for base in dna:
        p *= freqs[base]
    common_logs.append(round(common_log(p),3))
print(' '.join(map(str,common_logs)))
