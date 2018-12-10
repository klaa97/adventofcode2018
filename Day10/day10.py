import re
def check_if_final():
  for point in points:
    similar = False
    for to_confront in points:
      if (abs(to_confront[0] - point[0]) == 1 and abs(to_confront[1] - point[1]) == 1) or (to_confront[0] == point[0] and abs(to_confront[1] - point[1]) == 1) or (to_confront[1] == point[1] and abs(to_confront[0] - point[0]) == 1):
        similar = True
        break
    if similar == False:
      return False
  return True

with open("Day10/input") as fp:
    input = [list(map(int, re.findall('-?[0-9]+', line))) for line in fp]
points = [[i[0], i[1]] for i in input]
velocity = [[i[2], i[3]] for i in input]  
i=0
while True:
  min_y = min(points, key = lambda x: x[1])[1]
  max_y = max(points, key = lambda x: x[1])[1]
  min_x = min(points, key = lambda x: x[0])[0]
  max_x = max(points, key = lambda x: x[0])[0]
  if check_if_final():
    print(i)
    for y in range(min_y,max_y+1):
      for i in range(min_x,max_x+1):
        if [i,y] in points:
          print("X", end="")
        else:
          print(" ",end="")
      print("")
    break
  i=i+1
  for num, value in enumerate(points):
    points[num][0] = value[0] + velocity[num][0]
    points[num][1] = value[1] + velocity[num][1]
 
  
