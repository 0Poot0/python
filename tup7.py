tuple1=(1,2,3,[6,7],4,5)
print(tuple1[3][0])

list1=list(tuple1)
list1[3][0]=8
print(tuple(list1))