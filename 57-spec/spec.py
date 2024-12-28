#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

L = list(map(float,inp))

monoisotopic_mass_table = { "A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259, "F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406, "K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293, "P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203, "T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333 }

n = len(L)

def is_in_error_margin(val,target):
    err = 1/10000
    if val - (err * val) <= target and target <= val + (err * val):
        return True
    return False

def identify_protein(masses):
    protein = ""
    for m in reversed(range(1,len(masses))):
        current_mass = masses[m] - masses[m-1]
        for prot,monomass in monoisotopic_mass_table.items():
            if is_in_error_margin(current_mass,monomass):
                protein=prot+protein
                break # important break man
    return protein

print(identify_protein(L))
