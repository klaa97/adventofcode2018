#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def get_closest(x,y):
    if sum([abs(point[0]-x)+abs(point[1]-y) for point in coordinates]) < 10000:
        return 1
    else:
        return 0    
points = 0
with open('Day6/input', 'r') as fp:
    coordinates = fp.readlines()
coordinates = [(int(s.split(',')[0]),int(s.split(',')[1])) for s in coordinates]
l_min= min(coordinates,key=lambda x: x[0])[0]
l_max= max(coordinates,key=lambda x: x[0])[0]
w_min= min(coordinates,key=lambda x: x[1])[1]
w_max= max(coordinates,key=lambda x: x[1])[1]
for i in range(l_min,l_max+1):
    for j in range(w_min,w_max+1):
        points = points + get_closest(i,j)
print(points)


