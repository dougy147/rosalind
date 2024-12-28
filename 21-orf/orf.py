#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

dna_codon_table = { "TTT" : "F", "TTC" : "F", "TTA" : "L", "TTG" : "L", "TCT" : "S", "TCC" : "S", "TCA" : "S", "TCG" : "S", "TAT" : "Y", "TAC" : "Y", "TAA" : "Stop", "TAG" : "Stop", "TGT" : "C", "TGC" : "C", "TGA" : "Stop", "TGG" : "W", "CTT" : "L", "CTC" : "L", "CTA" : "L", "CTG" : "L", "CCT" : "P", "CCC" : "P", "CCA" : "P", "CCG" : "P", "CAT" : "H", "CAC" : "H", "CAA" : "Q", "CAG" : "Q", "CGT" : "R", "CGC" : "R", "CGA" : "R", "CGG" : "R", "ATT" : "I", "ATC" : "I", "ATA" : "I", "ATG" : "M", "ACT" : "T", "ACC" : "T", "ACA" : "T", "ACG" : "T", "AAT" : "N", "AAC" : "N", "AAA" : "K", "AAG" : "K", "AGT" : "S", "AGC" : "S", "AGA" : "R", "AGG" : "R", "GTT" : "V", "GTC" : "V", "GTA" : "V", "GTG" : "V", "GCT" : "A", "GCC" : "A", "GCA" : "A", "GCG" : "A", "GAT" : "D", "GAC" : "D", "GAA" : "E", "GAG" : "E", "GGT" : "G", "GGC" : "G", "GGA" : "G", "GGG" : "G", }

protein = ""
for line in inp[1:]:
    protein+=line.replace("\n","")

# For reverse complement
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

# ORF : Open Reading Frame
def find_open_reading_frame(protein):
    start_codon = ["ATG"]
    end_codon = ["TAG", "TGA", "TAA"]
    orf = set()
    translated_orf = set()
    protein_bak = protein
    for i in range(len(protein)):
        frame = ""
        translated_frame = ""
        reading = False
        p = protein_bak[i:]
        while p != "":
            if len(p) < 3: break
            codon = p[:3]
            if codon in start_codon and not reading:
                reading = True
                frame+=codon
                translated_frame+=dna_codon_table[codon]
                p = p[3:]
                continue
            elif codon in end_codon and reading:
                # print(frame,p)
                orf.add(frame)
                translated_orf.add(translated_frame)
                frame = ""
                translated_frame = ""
                p = p[3:]
                reading = False
                continue
            elif reading:
                frame+=codon
                translated_frame+=dna_codon_table[codon]
                p=p[3:]
                continue
            else:
                p=p[3:]
    #print(orf)
    return translated_orf

rev_protein = reverse_complement(protein)

candidates = set()
for cand in find_open_reading_frame(protein):
    candidates.add(cand)
for cand in find_open_reading_frame(rev_protein):
    candidates.add(cand)

for cand in candidates:
    print(cand)

# To sum up:
# Open reading frame has a mandatory "start codon" and stops at a mandatory "stop codon".
# However, while reading a frame, encountering a "start codon" does not stop it.
# Nevertheless, a "start codon" indicates that we COULD read the open reading frame
# from that point. (This is why I used sets, and read the whole protein one by one, and
# not by groups of three (not codon by codon).)
#
# Also, as DNA has two strands (double helix), with "opposite" (or parallel?) sequences
# of nucleotids (ex: "ATGC" - "TACG"), we can read open reading frame on this parallel
# strand too! That is why there is a "rev_protein" variable, that is the reverse comp.
