#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Found(Exception): pass
class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.chance = 0
def check_collision():
    for i in range(len(carts)):
        for j in range(len(carts)):
            if carts[i]!=carts[j] and carts[i].x == carts[j].x and carts[i].y == carts[j].y:
                carts.pop(i)
                carts.pop(j-1)
                return 1
    return None
def printmap():
    for y in range(len(paths)):
        for x in range(len(paths[y])):
            try:
                for i in carts:
                    if i.x == x and i.y == y:
                        raise Found
                print(paths[y][x],end="")
            except Found:
                print('*',end="")
        print("\n",end="")  

with open('Day13/input', 'r') as fp:
    paths = fp.readlines()
max_len = len(max(paths,key = lambda x: len(x)))
carts = []
#Extend the map
for y in range(len(paths)):
    paths[y] = list(paths[y])
    paths[y].extend(' '*(max_len - len(paths[y])))
for y in range(len(paths)):
    for x in range(len(paths[y])):
        if paths[y][x] == '>':
            carts.append(Cart(x,y,[1,0]))
            paths[y][x] = '-'
        elif paths[y][x] == '^':
            carts.append(Cart(x,y,[0,-1]))
            paths[y][x] = '|'
        elif paths[y][x] == 'v':
            carts.append(Cart(x,y,[0,1]))
            paths[y][x] = '|'
        elif paths[y][x] == '<':
            carts.append(Cart(x,y,[-1,0]))
            paths[y][x] = '-'
carts.sort(key=lambda x : [x.y,x.x])
i=0
while True:
    for cart in list(carts):
        if (paths[cart.y][cart.x] == '|' or paths[cart.y][cart.x] == '-'):
            cart.x = cart.x + cart.direction[0]
            cart.y = cart.y + cart.direction[1]
        elif (paths[cart.y][cart.x] == '/' or paths[cart.y][cart.x] == '\\'):
            if paths[cart.y][cart.x] == '/':
                reversal = 1
            else:
                reversal = -1
            if cart.direction == [1,0]:
                cart.direction = [0,reversal*-1]
            elif cart.direction == [-1,0]:
                cart.direction = [0,reversal*1]
            elif cart.direction == [0,1]:
                cart.direction = [reversal * -1,0]
            elif cart.direction == [0,-1]:
                cart.direction = [reversal * 1,0]
            cart.x = cart.x + cart.direction[0]
            cart.y = cart.y + cart.direction[1]
        elif (paths[cart.y][cart.x] == "+"):
            if cart.chance == 0:
                if cart.direction == [0,1]:
                    cart.direction = [1,0]
                elif cart.direction == [0,-1]:
                    cart.direction = [-1,0]
                elif cart.direction == [1,0]:
                    cart.direction = [0, -1]
                elif cart.direction == [-1,0]:
                    cart.direction = [0,1]
            elif cart.chance == 2:
                if cart.direction == [0,1]:
                    cart.direction = [-1,0]
                elif cart.direction == [0,-1]:
                    cart.direction = [1,0]
                elif cart.direction == [1,0]:
                    cart.direction = [0,1]
                elif cart.direction == [-1,0]:
                    cart.direction = [0,-1]
            cart.x = cart.x + cart.direction[0]
            cart.y = cart.y + cart.direction[1]
            cart.chance = (cart.chance + 1)%3
        if (check_collision() and len(carts) == 1):
            break
        if (len(carts)==1):
            print(carts[0].x,carts[0].y)
            raise Found
    carts.sort(key = lambda x: [x.y,x.x])
print(check_collision())

        
            




