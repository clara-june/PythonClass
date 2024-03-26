hrs = input("Enter Hours:")
rate = input("Enter Rate:")
hrs = float(hrs)
rate = float (rate)
print(hrs, rate)
if hrs > 40:
    print ('overtime')
    ot = hrs - 40
    print (ot)
    otp = ot * (rate * 1.5)
    print (otp)
    pay = rate * 40
    tpay = pay + otp
    print ('Total Pay:', tpay)
else:
    print ('regular')
    pay = hrs * rate
    tpay = pay 
    print ('Total Pay:', tpay)



