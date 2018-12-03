def evaluate(line):
  x,y = map(int, line[0].split(','))
  j,k = map(int, line[1].split('x'))
  for h in range(x,x+j):
    for l in range(y,y+k):
      if (fabric[h][l] == 0):
        fabric[h][l] = 1
      elif (fabric[h][l] == 1):
        global overlaps
        overlaps = overlaps + 1
        fabric[h][l] = 2     
overlaps = 0 
inputs=[]
fabric = [[0 for x in range(1000)] for y in range(1000)]
with open("input","r") as fp:
  inputs = [line.replace(' ',"").strip().split("@")[1].strip().split(':') for line in fp]
for claim in inputs:
  evaluate(claim)
print(overlaps)
