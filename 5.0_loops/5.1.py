num = 0
total = 0
while True :
    val = input('Enter a number:')
    if val == 'done':
        break
    try:
        fval = float(val)
        total = total + fval
        itotal = int(total)
        num = num + 1
    except:
        print ('Invalid input')
print (itotal,num,total/num)  