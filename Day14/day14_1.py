#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict
with open('Day14/input', 'r') as fp:
    input = int(fp.read())
scores = defaultdict(int)
scores[0] = 3
scores[1] = 7
len_scores = 2
elfs = [0,1]
while len_scores < input+10:
    list_sum = list(str(scores[elfs[0]]+scores[elfs[1]]))
    for i in list_sum:
        scores[len_scores] = int(i)
        len_scores = len_scores + 1
    for counter, i in enumerate(elfs):
        elfs[counter] = (elfs[counter] + 1 + scores[i])%len_scores
i = input
while i < len_scores:
    print(scores[i], end="")
    i= i+1



    

