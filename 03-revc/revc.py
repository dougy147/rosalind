#!/usr/bin/env python3
import sys, os
sys.path.insert(0, '../rosalind-helper/')
from rosalind_helper import *

# A - T
# C - G

def to_complement(s):
    if s == "\n": return ""
    complements = { "A": "T", "T": "A", "C": "G", "G": "C" }
    return complements[s]

def reverse(s):
    return ''.join(map(str,list(reversed(s))))

def reverse_complement(s):
    rc = ""
    for base in reverse(s):
        rc+=to_complement(base)
    return rc

print(reverse_complement(inp))
