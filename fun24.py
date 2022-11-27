def calculator(num1,num2,op):
    if op=='+':
        return num1+num2
    elif op=='-':
        return num1-num2
    elif op=='*':
        return num1*num2
    elif op=='/':
        return num1/num2



num1=float(input())
num2=float(input())
op=str(input("Enter an operator :"))
ans=calculator(num1,num2,op)
print(ans)