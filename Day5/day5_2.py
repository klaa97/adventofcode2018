from collections import defaultdict
with open("input","r") as fp:
  s = fp.read()
def fullyreact(poly):
  reacted = []
  for i in poly:
    if (len(reacted)!=0 and (reacted[-1] == chr(ord(i)-32) or (ord(i) <= 90 and reacted[-1] == chr(ord(i)+32)))):
      reacted.pop()
    else:
      reacted.append(i)
  return len(reacted)
chardict = defaultdict(int)
for char in range(65,91):
  fixed = s.replace(chr(char),"").replace(chr(char+32),"")
  fullyreacted = []
  for j in fixed:
    if (len(fullyreacted)!=0 and (fullyreacted[-1] == chr(ord(j)-32) or (ord(j) <= 90 and fullyreacted[-1] == chr(ord(j)+32)))):
      fullyreacted.pop()
    else:
      fullyreacted.append(j)
  chardict[char] = len(fullyreacted)
print(chardict[min(chardict,key=chardict.get)])
