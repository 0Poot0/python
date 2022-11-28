num=int(input())
string=""
num1=str(num)
for i in num1:
    if i!=num1[-1]:
        string+=i+","
    else:
        string+=i


print(string)