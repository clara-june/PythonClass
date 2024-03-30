fn = input('Enter a file: ')
if len(fn) < 1 : fn = 'mbox-short.txt'

fh = open(fn)
many = dict()
lst = list()
for line in fh:
    line = line.rstrip()

    if not line.startswith('From ') or len(line) < 3: continue

    time = line.split()[5]
    hour = time.split(':')[0]
    #print(hour)
    #print(sp)
    many[hour] = many.get(hour, 0) + 1   
#print(many)
for key, val in sorted(many.items()):
    print(key, val)
