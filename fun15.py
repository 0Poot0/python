def count(listOfNum):
    even=0
    odd=0
    for i in listOfNum:
        if i%2==0:
            even=even+1
        else:
            odd=+1
    return even,odd

listOfNum=[32,21,64,100,13]
even,odd=count(listOfNum)
print(even)
print(odd)
