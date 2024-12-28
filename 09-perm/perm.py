#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "auto"
from rosalind_helper import *

def factorial(n):
    m=1
    while n > 0:
        m*=n
        n-=1
    return m

def get_perms(n,expected_size,perm=[],stack=None):
    if stack == None: stack = []
    if len(perm) == expected_size:
        stack.append(perm)
        return
    for e in n:
        if e in perm: continue
        get_perms(n,expected_size,perm+[e],stack)
    return stack

def permutations(n):
    size = factorial(n)
    elems = [x for x in range(1,n+1)]
    perms = get_perms(elems, n)
    assert(size == len(perms))
    return (size, perms)

nb_perms, list_of_permutations = permutations(int(inp))
print(nb_perms)
for l in list_of_permutations:
    print(' '.join(map(str,l)))
