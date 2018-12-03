from collections import Counter
def take(claim, ids):
  x,y = map(int, claim[0].split(','))
  j,k = map(int, claim[1].split('x'))
  for h in range(x,x+j):
    for l in range(y,y+k):
      fabric[h][l].append(ids)
      if (len(fabric[h][l])>1):
        for i in fabric[h][l]:
          claims[i] = 0
inputs=[]
claims = []
fabric = [[[] for x in range(1000)] for y in range(1000)]
with open("input","r") as fp:
  inputs = [line.replace(' ',"").strip().split("@")[1].strip().split(':') for line in fp]
  claims = [1 for x in range(len(inputs)+1)]
claims[0] = 0
for counter, claim in enumerate(inputs,1):
  take(claim, counter)
print(claims.index(1))

