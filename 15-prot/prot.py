#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "auto"
from rosalind_helper import *

codon_table = { "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop", "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T", "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }

def codon_to_amino_acid(codon):
    return codon_table[codon]

amino = ""
while len(inp) > 0:
    codon = inp[:3]
    inp = inp[3:]
    a = codon_to_amino_acid(codon)
    if a == "Stop": break
    amino+=a

print(amino)
