#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "auto"
from rosalind_helper import *

couples_dominant_offsprings = [
        2*(1/1),  # AA-AA
        2*(1/1),  # AA-Aa
        2*(1/1),  # AA-aa
        2*(3/4),  # Aa-Aa
        2*(1/2),  # Aa-aa
        2*0,      # aa-aa
        ]

couples = list(map(int,inp.split(" ")))

offsprings = 0
for i in range(len(couples)):
    offsprings+=couples[i] * couples_dominant_offsprings[i]
print(offsprings)
