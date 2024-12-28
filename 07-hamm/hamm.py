#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

def hamm_distance(s,t):
    hamm = 0
    for i in range(len(s)):
        if s[i] != t[i]: hamm+=1
    return hamm

s, t = inp
print(hamm_distance(s,t))
