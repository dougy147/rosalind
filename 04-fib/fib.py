#!/usr/bin/env python3
import sys, os
sys.path.insert(0, '../rosalind-helper/')
from rosalind_helper import *

def rabbit_fib(n,k):
    def r(a,b,i,n):
        if i == n: return a
        return r(b,b+k*a,i+1,n)
    return r(1,1,1,n)

a, b = inp.split(" ")
print(rabbit_fib(int(a),int(b)))
