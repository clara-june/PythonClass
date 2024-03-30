fn = input('Enter a file: ')
fh = open(fn)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From ') or len(line) < 3: continue
    count = count + 1
    sp = line.split()
    email = sp[1]
    print(email)
print('There were', count, 'lines in the file with From as the first word')