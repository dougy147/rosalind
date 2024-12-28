#!/usr/bin/env python3
import sys, os
sys.path.insert(0, '../rosalind-helper/')
from rosalind_helper import *

alphabet = ["A","C","G","U"]

def dna_to_rna(dna_string):
    rna=""
    for base in dna_string:
        if base == "T": rna+="U"
        else: rna+=base
    return rna

print(dna_to_rna(inp))
