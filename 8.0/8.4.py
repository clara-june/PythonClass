fname = input('Enter file name:')
fh = open(fname)
lst = list()
for line in fh:
    #print(line)
    wrds = line.split()
    for word in wrds:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
