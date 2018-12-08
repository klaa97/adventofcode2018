#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict
class Node():
    def __init__(self,n_node,nchilds, nmetadata):
        self.nchilds = nchilds
        self.nmetadata = nmetadata
        self.n_node = n_node
    def set_metadata(self,metadata):
        self.metadata = metadata
    def set_childs(self,childs):
        self.childs = childs
    def get_value(self):
        if self.nchilds != 0:
            self.value = 0
            for i in self.metadata:
                if len(self.childs) >= i and i != 0:
                    self.value = self.value + (self.childs[i-1]).get_value()
            return self.value
        else:
            return sum(self.metadata) 

with open('Day8/input', 'r') as fp:
    input = list(map(int,fp.read().strip().split(' ')))
nodes = []
i=0
n_node = 0
temp_nodes = []
current_child = defaultdict(int)
childs = defaultdict(list)
while i < len(input):
    while(temp_nodes):
        if (current_child[temp_nodes[-1]] == nodes[temp_nodes[-1]].nchilds):
            metadata = []
            for j in range(i, i + nodes[temp_nodes[-1]].nmetadata):
                metadata.append(input[j])
            nodes[temp_nodes[-1]].set_metadata(metadata)
            i = i + nodes[temp_nodes[-1]].nmetadata
            nodes[temp_nodes[-1]].set_childs(childs[temp_nodes[-1]])
            temp_nodes.pop()
        else:
            current_child[temp_nodes[-1]] = current_child[temp_nodes[-1]] + 1
            break
    if (i<len(input)):
        nchilds = input[i]
        nmetadata = input[i+1]
        metadata = []
        if (nchilds != 0):
            temp_nodes.append(n_node)
            nodes.append(Node(n_node,nchilds,nmetadata))
            if (len(temp_nodes) >= 2 and current_child[temp_nodes[-2]] != 0):
                childs[temp_nodes[-2]].append(nodes[-1])
            i = i + 2
        else:
            for j in range(i+2, i + 2 + nmetadata):
                metadata.append(input[j])
            nodes.append(Node(n_node,nchilds,nmetadata))
            nodes[-1].set_metadata(metadata)
            if (current_child[temp_nodes[-1]] != 0):
                childs[temp_nodes[-1]].append(nodes[-1])
            i = i + 2 + nmetadata
        n_node = n_node + 1
print(sum(sum(i.metadata)for i in nodes))
print(nodes[0].get_value())