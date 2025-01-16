#!/usr/bin/env python3
import sys
sys.path.insert(0, '../aoc-helper/')
readfile_mode = "auto"
sys.setrecursionlimit(10**6)
from aoc_helper import *

A = list(map(float,inp.split(" ")))

import math # need sqrt()
probs = []
for a in A:
    p = math.sqrt(a) # proba to get recessive on one chromosome
    probs.append(1 - ((1-p)**2))
print(' '.join(map(str,probs)))
