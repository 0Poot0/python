a=int(input("Enter side 1:"))
b=int(input("Enter the side 2 :"))
c=int(input("Enter the side 3 :"))
if c<a+b and b<a+b and a<b+c:
    print("possible")

else:
    print("Not possible")