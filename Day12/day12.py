import re
with open("Day12/input") as fp:
  input = fp.readlines()
state = re.findall('[#.]+',input[0])[0]
rules = [re.split(' ', line)[0] for line in input[2:] if re.search('#$',line)]
start_number = 2
state = "."*4 + state + '.'*4
state = list(state)
new_state = state.copy()
start_number = 4
old_total = 0
for gen in range(1000):
  for pot in range(2, len(state)-2 ):
    if ''.join(state[pot-2:pot+3]) in rules:
      new_state[pot] = '#'
    else:
      new_state[pot] = '.'
  first = new_state.index('#')
  first = 4 if first > 4 else 4
  start_number = start_number + 4- first
  for i in range(4-first):
    new_state.insert(0,'.')
  last = ''.join(new_state).rindex('#')
  for i in range(last + 4 - len(state)):
    new_state.append('.')
  state = new_state.copy()
  total = 0
  for counter,i in enumerate(state):
    if i == '#':
      total = total + counter - start_number
  if (gen == 19):
    #Part1
    print(total)
  diff = total - old_total
  old_total = total
#Part2
print(total+diff*(50000000000-1000))
