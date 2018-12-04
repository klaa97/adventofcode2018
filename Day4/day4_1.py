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
    for signals in i[1]:
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
max_id = max(totalsleep,key = lambda x: totalsleep.get(x)[0])
#Part 1
print(max_id*max(totalsleep[max_id][1],key= lambda x: totalsleep[max_id][1].get(x)))
#Part 2
minute_for_guard = defaultdict(list)
for i in totalsleep.items():
    try: 
        max_minute = max(i[1][1], key = lambda x: i[1][1].get(x))
        minute_for_guard[i[0]].append(max_minute)
        minute_for_guard[i[0]].append(i[1][1].get(max_minute))
    except:
        pass
max_id_minute = max(minute_for_guard, key = lambda x: minute_for_guard.get(x)[1])
max_minute = minute_for_guard[max_id_minute][0]
print(max_id_minute*max_minute)

    