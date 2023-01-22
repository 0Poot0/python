#a="Hello"
#b=['a','b','c']
#print("length of list is : ",len(b))
#same function doing the same work for different datas.

def add(a,b,c=4):
    return a+b+c

#method overloading
print(add(1,2))
print(add(1,2,3))