#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict
def get_closest(x,y):
    temp_freq = []
    for point in coordinates:
        temp_freq.append(abs(point[0]-x)+abs(point[1]-y))
    max_coord = list(filter(lambda x: x == min(temp_freq),temp_freq))
    if (len(max_coord)==1 and temp_freq.index(min(temp_freq)) not in blacklist):
        freq[temp_freq.index(min(temp_freq))] = freq[temp_freq.index(min(temp_freq))] + 1
        if (x==l_min or x ==l_max or y == w_min or y == w_max):
            freq.pop(temp_freq.index(min(temp_freq)),None)
            blacklist.add(temp_freq.index(min(temp_freq)))
blacklist = set()
freq = defaultdict(int)
with open('Day6/input', 'r') as fp:
    coordinates = fp.readlines()
coordinates = [(int(s.split(',')[0]),int(s.split(',')[1])) for s in coordinates]
l_min= min(coordinates,key=lambda x: x[0])[0]
l_max= max(coordinates,key=lambda x: x[0])[0]
w_min= min(coordinates,key=lambda x: x[1])[1]
w_max= max(coordinates,key=lambda x: x[1])[1]
table = defaultdict(lambda: defaultdict(dict))
for i in range(l_min,l_max+1):
    for j in range(w_min,w_max+1):
        get_closest(i,j)
print(freq[max(freq)])


