fn = input('Enter a file: ')
if len(fn) < 1 : fn = 'mbox-short.txt'

fh = open(fn)
many = dict()
for line in fh:
    line = line.rstrip()

    if not line.startswith('From ') or len(line) < 3: continue

    sp = line.split()
    #print(sp)
    email = sp[1]
    
    many[email] = many.get(email, 0) + 1   
#print(many)

largest = None
largeemail= None
for e, t in many.items() :
    #print(e, t)
    if largest is None or largest < t:
        largest = t
        largeemail = e
print(largeemail, largest)