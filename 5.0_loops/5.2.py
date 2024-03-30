largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == "done":
        break
    try: 
        gum = float(num)
    except: 
        print('Invalid input')
        continue
    if largest is None:
        largest = gum
    elif gum > largest:
        largest = gum
    if smallest is None:
        smallest = gum  
    elif gum < smallest:
        smallest = gum
print(largest , smallest)