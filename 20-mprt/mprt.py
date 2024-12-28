#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "line"
from rosalind_helper import *

import requests

# N-glycosylation : N{P}[ST]{P}
# {P} means anything but not P
# [ST] means either S or T

def fetch_protein(protein):
    url = f"https://rest.uniprot.org/uniprotkb/{protein}.fasta"
    headers = ""
    protein_string = ""
    for line in requests.get(url).text.split("\n"):
        if " " in line:
            headers += line
        else: protein_string+=line
    return protein_string

# Realising "import re" is not good
def is_Nglycosylation(sub):
    a,b,c,d = sub
    if a == "N" and b != "P" and (c == "S" or c == "T") and d != "P":
        return True
    return False

def find_Nglycosylation(protein_str):
    pattern = "N[^P](S|T)[^P]"
    indexes = []
    index = 1
    while protein_str != "":
        if len(protein_str) < 4: break
        sub = protein_str[:4]
        if is_Nglycosylation(sub):
            indexes.append(index)
        protein_str=protein_str[1:]
        index+=1
    if indexes == []: return ""
    return " ".join(map(str,indexes))

for protein in inp:
    protein_basename = protein.split("_")[0]
    protein_str = fetch_protein(protein_basename)
    indexes = find_Nglycosylation(protein_str)
    if not indexes == "":
        print(protein)
        print(indexes)
