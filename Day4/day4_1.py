#[1518-11-01 00:00] Guard #10 begins shift
#[1518-11-01 00:05] falls asleep
#[1518-11-01 00:25] wakes up
from collections import defaultdict
import re
inputs = []
with open("Day4/input") as fp:
    inputs = fp.readlines()
inputs.sort()
logstemp = list(map(lambda x: [list(map(int,re.split('-|-| |:',x[0].replace('[','')))), list(map(str, re.findall(r'[0-9]+|falls|wakes',x[1])))],list(map(lambda x: x.split(']'),inputs))))
logs = defaultdict(list)
for i in logstemp:
    if (i[1][0].isdigit()):
        currentid = int(i[1][0])
        i[1][0] = 'wakes'
        logs[currentid].append(i)
    logs[currentid].append(i)
totalsleep = defaultdict(list)
for i in logs.items():
    totalsleep[i[0]].append(0)
    noawakeday=set()
    number_of_sleeps = defaultdict(int)
    currentmin = 0
    awake = False
    for counter,signals in enumerate(i[1]):
        if (signals[1][0] == 'falls'):
            awake = False
            currentmin = signals[0][4]
        elif (awake == False and signals[1][0] == 'wakes'):
            totalsleep[i[0]][0]=totalsleep[i[0]][0] + (signals[0][4] - currentmin)
            noawakeday.update(range(currentmin, signals[0][4]))
            awake = True
        elif (awake == True and signals[1][0] == 'wakes'):
            for j in noawakeday:
                number_of_sleeps[j] = number_of_sleeps[j] + 1
            noawakeday=set()
    totalsleep[i[0]].append(number_of_sleeps)
for i in totalsleep.items():
    print(i)
max_id = max(totalsleep,key = lambda x: totalsleep.get(x)[0])
print(max_id*max(totalsleep[max_id][1],key= lambda x: totalsleep[max_id][1].get(x)))



        

    
    