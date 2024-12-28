#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

rna = ''.join(map(str,inp[1:])).replace("\n","")

ratio = { "U": rna.count("U"), "A": rna.count("A"), "G": rna.count("G"), "C": rna.count("C") }

bondings_ua = arrangements(min(ratio["U"],ratio["A"]),max(ratio["U"],ratio["A"]))
bondings_gc = arrangements(min(ratio["G"],ratio["C"]),max(ratio["G"],ratio["C"]))

print(bondings_ua*bondings_gc)
