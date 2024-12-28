#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "auto"
from rosalind_helper import *

def get_perms(n):
    def gp(n,expected_length,perms=[],stack=None):
        if stack == None: stack = []
        if len(perms) == expected_length:
            if not perms in stack:
                stack.append(perms)
            return
        for elem in n:
            if elem in perms or elem * -1 in perms: continue
            gp(n,expected_length,perms+[elem*-1],stack)
            gp(n,expected_length,perms+[elem],stack)
        return stack
    perms = gp(n,len(n))
    return (len(perms),perms)

lst = [x for x in range(1,int(inp)+1)]
nb, lst_signed_perms = get_perms(lst)
print(nb)
for l in lst_signed_perms:
    print(' '.join(map(str,l)))
