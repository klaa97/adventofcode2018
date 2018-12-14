#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict
class Found(Exception): pass
def check_scores():
    i = len_scores-len(input)
    j = 0
    while i < len_scores:
        if (scores[i] != input[j]):
            return None
        else:
            i = i+1
            j = j+1
    return 1 
with open('Day14/input', 'r') as fp:
    input = [int(x) for x in fp.read()[:-1]]
input = [int(x) for x in input]
scores = defaultdict(int)
scores[0] = 3
scores[1] = 7
len_scores = 2
elfs = [0,1]
while True:
    i = 0
    list_sum = list(str(scores[elfs[0]]+scores[elfs[1]]))
    for i in list_sum:
        scores[len_scores] = int(i)
        len_scores = len_scores + 1
        if (len_scores >= len(input)):
            if (check_scores()):
                print(len_scores-len(input))
                raise Found
    for counter, i in enumerate(elfs):
        elfs[counter] = (elfs[counter] + 1 + scores[i])%len_scores



    

