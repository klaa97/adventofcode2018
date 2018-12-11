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
current_max = [[-1,-1],-1]
for y in range(1,299):
    for x in range(1,299):
        total = 0
        for i in range(y,y+3):
            for k in range(x,x+3):
                total = total + powers[k][i]
        if total >= current_max[1]:
            current_max = [[x,y],total]
print(current_max)

