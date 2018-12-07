#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Step U must be finished before step C can begin.
import re
from collections import defaultdict 
with open('Day7/input', 'r') as fp:
    input = fp.readlines()
completed = defaultdict(int)
todo = defaultdict(int)
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
    todo[i[0]] = -1
    completed[i[0]] = 60 + ord(i[0])-ord('A')+1
    completed[i[1]] = 60 + ord(i[1])-ord('A')+1
    states.add(i[0])
    states.add(i[1])
seconds = 0
queue = []
while states:
    current_states = set()
    tmp_queue = []
    current_states.update(states)
    for i in states:
        for j in couples:
            if j[1] == i and todo[j[0]] == -1:
                current_states.remove(i)
                break
    tmp_queue.extend(sorted(current_states))
    tmp_queue = list(dict.fromkeys(tmp_queue))[0:5]
    queue = tmp_queue.copy()
    for i in queue:
        completed[i] = completed[i] - 1
        if completed[i] == 0:
            todo[i[0]] = 0
            states.remove(i)
            tmp_queue.remove(i)
    seconds = seconds + 1
print(seconds)
