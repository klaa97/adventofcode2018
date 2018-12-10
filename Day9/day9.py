#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import OrderedDict
from collections import defaultdict
import re
class Node:
    def __init__(self,value,prev = None, nextt = None):
        self.value = value
        if (prev is None or nextt is None):
            self.next = self
            self.prev = self
        else:
            self.next = nextt
            self.prev = prev
    def print(self):
        print("Io sono %d, prima c'è %d, dopo c'è %d" % (self.value, self.prev.value,self.next.value))
with open('Day9/input', 'r') as fp:
    nplayers, maxmarble = map(int,re.findall('[0-9]+',fp.read()))
players = defaultdict(int)
current_marble = Node(0)
marble = 1
cur_player = 0
maxmarble = maxmarble * 100 #comment this line for part 1
while marble <= maxmarble:
    if (marble % 23 != 0):
        current_marble.next.next = Node(marble, current_marble.next,current_marble.next.next)
        current_marble.next.next.next.prev = current_marble.next.next
        current_marble = current_marble.next.next
        marble = marble + 1
    else:
        for i in range(7):
            current_marble = current_marble.prev
        players[cur_player] = players[cur_player] + marble + current_marble.value
        new_marble = current_marble.next
        current_marble.prev.next = new_marble
        current_marble = new_marble
        marble = marble + 1
    cur_player = (cur_player + 1) % nplayers
print(max(players.values()))