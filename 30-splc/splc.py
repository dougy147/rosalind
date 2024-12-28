#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

dna = ""
parsed_first = False

introns = []
intron = ""
c = 0
for l in inp:
    if ">" in l:
        if c > 0: parsed_first = True
        if parsed_first and intron != "":
            introns.append(intron)
            intron = ""
        c+=1
        continue
    else:
        if not parsed_first: dna+=l
        else: intron+=l
introns.append(intron)

def remove_introns(dna,introns):
    epurated = ""

    while len(dna) > 0:
        found = False
        for intron in sorted(introns,key=len,reverse=True):
            if len(intron) > len(dna): continue
            if dna[:len(intron)] == intron:
                found = True
                dna = dna[len(intron):]
                break
        if not found:
            epurated += dna[0]
            dna = dna[1:]
    return epurated

# String to amino acid
codon_table = { "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop", "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T", "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", }
def codon_to_amino_acid(codon):
    return codon_table[codon]
def protein_to_amino_acid(protein):
    amino = ""
    while len(protein) > 0:
        codon = protein[:3]
        protein = protein[3:]
        a = codon_to_amino_acid(codon)
        if a == "Stop": break
        amino+=a
    return amino

def dna_to_rna(dna_string):
    rna=""
    for base in dna_string:
        if base == "T": rna+="U"
        else: rna+=base
    return rna

exons = remove_introns(dna,introns)
print(protein_to_amino_acid(dna_to_rna(exons)))
