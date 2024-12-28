#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "line"
from rosalind_helper import *

alphabet = inp[0].split(" ")
n = int(inp[1])

def draw_replace(alphabet,n,current=[],stack=None):
    if stack == None: stack = []
    if n == 0:
        stack.append(current)
        return
    for i in range(len(alphabet)):
        draw_replace(alphabet,n-1,current + [alphabet[i]],stack)
    return stack

for x in draw_replace(alphabet,n):
    print(''.join(map(str,x)))
