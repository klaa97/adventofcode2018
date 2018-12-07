#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Step U must be finished before step C can begin.
import re
from collections import defaultdict 
with open('Day7/input', 'r') as fp:
    input = fp.readlines()
completed = defaultdict(int)
steps = []
couples = [re.findall("[A-Z]",i[1:]) for i in input]
states = set()
added = True
while added == True:
    added = False
    new_elems = couples.copy()
    for i in couples:
        for j in couples:
            if ((i[0] != j[0] or i[1] != j[1])) and (i[1] == j[0]) and [i[0],j[1]] not in couples and [i[0],j[1]] not in new_elems:
                added = True
                new_elems.append([i[0],j[1]])
    couples.extend(new_elems)
for i in couples:
    completed[i[0]] = -1
    states.add(i[0])
    states.add(i[1])
while states:
    current_states = set()
    current_states.update(states)
    for i in states:
        for j in couples:
            if j[1] == i and completed[j[0]] == -1:
                current_states.remove(i)
                break
    next_step = min(current_states)
    steps.append(next_step)
    completed[next_step] = 0
    states.remove(next_step)
print(''.join(steps))
