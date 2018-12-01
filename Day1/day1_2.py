import itertools
inputs = []
sums = []
with open("Day1/input","r") as fp:
    inputs = fp.readlines()
inputs = list(map(lambda x: int(x.split('\n')[0]), inputs))
sums = itertools.accumulate(itertools.chain.from_iterable(itertools.repeat(inputs)))
found = set()
for i in sums:
    if i in found:
        print(i)
        break
    found.add(i)