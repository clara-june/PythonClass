import re
lst = list()
x = 0
count = 0
fn = input('Enter a file: ')
if len(fn) < 1 : fn = 'regex_sum_42.txt'

fh = open(fn)
for line in fh:
    line = line.rstrip()
    stuff = re.findall('[0-9*]+', line)
    if len(stuff) < 1 : continue
    #print(stuff)
    count = count + 1
    for match in stuff:
        num = float(match)
        lst.append(num)
for num in lst:
    x = x + num
#print(len(lst))
print(x)