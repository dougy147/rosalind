#!/usr/bin/env python3
import sys
sys.path.insert(0, '../aoc-helper/')
readfile_mode = "auto"
sys.setrecursionlimit(10**6)
from aoc_helper import *

import math
A = list(map(float,inp.split(" ")))
probs = []
for a in A:
    p_male = a # for a male, proportion == proba!
    female_prob = 1 - ((p_male**2) + ((1-p_male)**2))
    probs.append(female_prob)
print(" ".join(map(str,probs)))
