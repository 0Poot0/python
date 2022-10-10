yearsOfWorking= int(input("Enter your years of service :"))
salary= float(input("What is your salary ? : "))
if yearsOfWorking>=5:
    new_salary=salary + 1000 #bonus salary is 1000Rs
    print("Your new salary is ",new_salary)
else:
    print("Oops! you will not get any bonus . Your salary is", salary )