def computepay(hours, rate):
    if hours > 40:
        ot = hours - 40
        otp = ot * (rate * 1.5)
        pay = rate * 40
        tpay = pay + otp
       
    else:
        pay = hours * rate
        tpay = pay 
       
    return tpay

hrs = input("Enter Hours:")
rte = input("Enter Rate:")
hrs = float(hrs)
rte = float (rte)
xp = computepay(hrs, rte)
print("Pay:", xp)






