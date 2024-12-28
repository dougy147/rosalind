#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

raw = {}
fastas = {}
new_fast = False
for line in inp:
    if ">" in line:
        new_fast = True
        key = str(line).replace(">","")
        cur_len = 0
        cur_size = 0
    else:
        new_fast = False
    if not new_fast:
        cur_len += len([x for x in line if x == "C" or x == "G"])
        cur_size += len(line)
        fastas[str(key)] = cur_len / cur_size * 100

highest_gc = -1
for k in fastas:
    if fastas[k] > highest_gc:
        highest_label = k
        highest_gc = fastas[k]
print(highest_label)
print(highest_gc)
