#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

dna = ''.join(map(str,inp[1:])).replace("\n","")

def rev_comp(s):
    rev = ""
    for i in reversed(range(len(s))):
        c = s[i]
        match c:
            case "A": rev+="T"
            case "T": rev+="A"
            case "G": rev+="C"
            case "C": rev+="G"
    return rev

def palindrome_loc(s):
    # return substrings of size 4 and 12 from s
    for i in range(len(s)):
        for k in range(4,12+1):
            if i + k > len(s): continue
            sub = s[i:i+k]
            if sub == rev_comp(sub): print(i+1,k) # print i+1 because they index starting from 1

palindrome_loc(dna)
