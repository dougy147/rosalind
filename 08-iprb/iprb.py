#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
from rosalind_helper import *

inp = inp[0].split(" ")
k,m,n = map(int,inp)

def prob(k,m,n):
    t = k+m+n
    a = k/t
    b = ((m/t) * (k/(t-1))) + (0.75 * (m/t) * ((m-1)/(t-1))) + (0.5 * (m/t) * (n/(t-1)))
    c = ((n/t) * (k/(t-1))) + (0.5 * (n/t) * (m/(t-1)))
    return a + b + c

print(prob(k,m,n))
