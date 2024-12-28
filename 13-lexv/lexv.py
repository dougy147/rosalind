#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "line"
from rosalind_helper import *

alphabet = inp[0].split(" ")
n = int(inp[1])

lexico_order = {}
for i,a in enumerate(alphabet):
    lexico_order[a] = i

def draw_with_replacement_in_order_of_alphabet(alphabet,n,current=[],stack=None):
    if stack == None: stack = []
    if n == 0:
        stack.append(current)
        return
    for i in range(len(alphabet)):
        letter = alphabet[i]
        draw_with_replacement_in_order_of_alphabet(alphabet,n-1,current + [letter],stack)
    return stack

strings = []
for i in range(1,n+1):
    for elem in draw_with_replacement_in_order_of_alphabet(alphabet,i):
        strings.append(''.join(map(str,elem)))

def string_to_score(string):
    conv = ""
    for s in string:
        conv+=str(lexico_order[s])
    return conv

def score_to_string(score):
    conv = ""
    for s in score:
        for k in lexico_order:
            if lexico_order[k] == int(s):
                conv+=k
                break
    return conv

converted = []
for s in strings:
    converted.append(string_to_score(s))
strings = []
for s in sorted(converted):
    strings.append(score_to_string(s))

for s in strings:
    print(s)
