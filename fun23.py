def calculator(num1,num2,op):
    if op=='+':
        print(num1+num2)
    elif op=='-':
        print(num1-num2)
    elif op=='*':
        print(num1*num2)
    elif op=='/':
        print(num1/num2)



num1=float(input())
num2=float(input())
op=str(input("Enter an operator :"))
calculator(num1,num2,op)
