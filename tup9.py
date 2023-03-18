tuple1=(10,20)
tuple2=(30,40)

#list1=list(tuple1)
#list2=list(tuple2)
#temp=list1
#list1=list2
#list2=temp
#print(tuple(list1))
#print(tuple(list2))

temp=tuple2
tuple2=tuple1
tuple1=temp
print(tuple1)
print(tuple2)