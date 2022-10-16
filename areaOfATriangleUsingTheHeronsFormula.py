a=float(input("Enter the length for the first side of the triangle(A) : "))
b=float(input("Enter the length for the second side of the triangle(B) :"))
c=float(input("Enter the length for the third side of the triangle(C) :"))
s= (a+b+c)/2 #s is the semi perimeter
area = (s*((s-a)*(s-b)*(s-c)))**0.5
print("The area of the triangle using the Heron's formula is :",area)