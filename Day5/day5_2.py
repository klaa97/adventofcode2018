from collections import defaultdict
with open("input","r") as fp:
  s = fp.read()
chardict = defaultdict(int)
for char in range(65,91):
  fixed = s.replace(chr(char),"").replace(chr(char+32),"")
  fullyreacted = []
  for j in fixed:
    if (len(fullyreacted)!=0 and ((ord(j) > 90 and fullyreacted[-1] == chr(ord(j)-32)) or (ord(j) <= 90 and fullyreacted[-1] == chr(ord(j)+32)))):
      fullyreacted.pop()
    else:
      fullyreacted.append(j)
  chardict[char] = len(fullyreacted)
print(chardict[min(chardict,key=chardict.get)])
