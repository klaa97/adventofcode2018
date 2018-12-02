import itertools
import collections
inputs = []
with open("Day2/input") as fp:
    inputs = fp.readlines()
inputs = list(map(lambda x:  collections.Counter(x),inputs))
num_of_two = sum(map(lambda x: 1 if any(c == 2 for c in x.values()) else 0,inputs))
num_of_three = sum(map(lambda x: 1 if any(c == 3 for c in x.values()) else 0,inputs))
print(num_of_two*num_of_three)
