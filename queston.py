#take a user input if the len of the str is greater 3 characters
#  then add -ing as at the end of that otherwise print it as it is. 
a=str(input("Enter any sentence : "))
if len(a)>3:
    print(a+"ing")
else:
    print(a)