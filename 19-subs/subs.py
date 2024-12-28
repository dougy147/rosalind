#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

s,t = inp

indexes = []
for i in range(len(s)-len(t)):
    if s[i:i+len(t)] == t: indexes.append(i+1)
print(" ".join(map(str,indexes)))
