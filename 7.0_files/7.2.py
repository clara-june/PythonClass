fn = input('Enter file name:')
fh = open(fn)
total = 0
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    num = line.find(':')
    nnum = float(line[num+1:])
    total = total + nnum
    count = count + 1
print('Average spam confidence: ' + str(total/count))
