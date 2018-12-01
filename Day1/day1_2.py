import itertools
from collections import Counter
inputs = []
sums = []
with open("Day1/input","r") as fp:
    inputs = fp.readlines()
inputs = list(map(lambda x: int(x.split('\n')[0]), inputs))
sums = itertools.accumulate(itertools.chain.from_iterable(itertools.repeat(inputs)))
seen = set()
for i in sums:
    if i in seen:
        print(i)
        break
    seen.add(i)