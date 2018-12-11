#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict

def power(x,y):
    rack_id = x + 10
    temp_result = (rack_id*y+serial)*rack_id
    if len(str(temp_result))>=3:
        temp = str(temp_result)[-3]
    else:
        temp = 0
    return int(temp) - 5
powers = defaultdict(lambda : defaultdict(int))
with open('Day11/input', 'r') as fp:
    serial = int(fp.read())
for i in range(1,301):
    for j in range(1,301):
        powers[i][j] = power(i,j)
current_max = [[-1,-1],-1,-1]
for y in range(1,301):
    for x in range(1,301):
        total = powers[x][y]
        if total >= current_max[1]:
            current_max = [[x,y],total,1]
        for i in range(1,min(301-y,301-x)):
            for k in range(0,i):
                total = total + powers[x+i][y+k]
                total = total + powers[x+k][y+i]
            total = total + powers[x+i][y+i]
            if total >= current_max[1]:
                current_max = [[x,y],total,i+1]
print(current_max)

