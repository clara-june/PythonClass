def Findsmall(itr,ele,list1): #recursive function to find smallest number

  if itr == len(list1):        #base condition

    print("The smallest number in the list is " ,ele)

    return

  if list1[itr]<ele: #check the current element less than minimum or not

    ele  =  list1[itr]

  Findsmall(itr+1,ele,list1) #recursive function call

  return

#driver code

lis=[5,7,2,8,9]

ele = lis[0]

Findsmall(0,ele,lis)