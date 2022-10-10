workingDays=int(input("Enter the number of working days : "))
totalDays=int(input("Enter the number of total days : "))
percentage=(workingDays/totalDays)*100
if percentage>=75:
    print("Your attendance is ",percentage ,"%.You are eligible to give the exam."
    )
else:
    print("Your attendance is only ",percentage,"% .You are not eligible to give the exam.")