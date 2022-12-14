#def isEven(i):
 #   return i%2==0



from functools import reduce 

list1=[10,20,30,40,50]
#output=list(filter(isEven,list1))
#print(output)

#output1=list(filter(lambda i:i>15,list1))
#print(output1)

#output3=list(map(lambda i:i**0.5,list1))
#print(output3)

#output4=reduce(lambda a,b: a+b,list1)
#print(output4) 

#output1=list(map(lambda i:i*3,list1))
#print(output1)

list2=[34,88,30,22,10,15,18]
output5=list(filter(lambda i:i%5==0,list2)) 
print(output5)
