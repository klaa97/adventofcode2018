with open("input","r") as fp:
  s = fp.read()
reacted = []
for i in s:
  if (len(reacted)!=0 and ((ord(i) > 90 and reacted[-1] == chr(ord(i)-32)) or (ord(i) <= 90 and reacted[-1] == chr(ord(i)+32)))):
    reacted.pop()
  else:
    reacted.append(i)
print(len(reacted))
