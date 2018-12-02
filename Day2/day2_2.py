import itertools
def trim_different_char(string1, string2):
    string3 = ''.join(c1 for c1,c2 in zip(string1,string2) if c1==c2)
    if len(string3) == len(string1) - 1 and len(string1) == len(string2):
        return string3
inputs = []
with open("Day2/input") as fp:
    inputs = fp.readlines()
inputs = [i.strip().split("\n")[0] for i in inputs]
couples = itertools.combinations(inputs,2)
correct_couples =set(trim_different_char(i[0],i[1]) for i in couples)
print(list(filter(None.__ne__, correct_couples))[0])