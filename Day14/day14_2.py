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
scores = defaultdict(int)
scores[0] = 3
scores[1] = 7
len_scores = 2
first_elf = 0
second_elf = 1
while True:
    list_sum = [int(d) for d in str(scores[first_elf]+scores[second_elf])]
    for i in list_sum:
        scores[len_scores] = i
        len_scores = len_scores + 1
        if (len_scores >= len(input)):
            if (check_scores()):
                print(len_scores-len(input))
                raise Found
    first_elf = (first_elf + 1 + scores[first_elf])%len_scores
    second_elf = (second_elf + 1 + scores[second_elf])%len_scores



    

