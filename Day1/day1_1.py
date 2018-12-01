inputs = []
with open("Day1/input","r") as fp:
    inputs = fp.readlines()
total = sum(map(lambda x: int(x.split('\n')[0]), inputs))
print(total)
