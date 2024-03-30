try:
    Hrs= float(input('Enter Hours:'))
    Rate= float(input('Enter Rate:'))
    if Hrs>40:
        Pay= ((Hrs-40) * Rate * 1.5) + (40 * Rate)
    if Hrs<=40:
         Pay= Hrs * Rate 
    print('Pay:',Pay)
except:
    print('Error, please enter numeric input')