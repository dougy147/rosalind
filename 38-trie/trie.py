#!/usr/bin/env python3
import sys
sys.path.insert(0, '../rosalind-helper/')
readfile_mode = "lines"
sys.setrecursionlimit(10**6)
from rosalind_helper import *

dnas = inp

#           /   \
#         A      G
#         T      A
#       A   C    T
#       G
#       A

#node(label, parent, number , [childs])
#leaf(label, parent, number , [])

class Node:
    def __init__(self, label, nb, parent, childs=None):
        if childs == None: childs = []
        self.label = label
        self.nb = nb # nb of nodes added so far
        self.parent = parent # Node
        self.childs = childs # Node(s)
        self.append_self_to_parent()
    def append_self_to_parent(self):
        if self.label == "ROOT": return
        self.parent.childs.append(self)

root = Node("ROOT",1,"no_parent")

nodes = [root]
for d in dnas:
    prev = root
    for i in range(len(d)):
        if not d[i] in [child.label for child in prev.childs]:
            node = Node(d[i],len(nodes)+1,prev)
            nodes.append(node)
        else:
            index = [child.label for child in prev.childs].index(d[i])
            node = prev.childs[index]
            assert(d[i] == node.label)
        prev = node

for node in nodes[1:]:
    print(node.parent.nb,node.nb,node.label)
