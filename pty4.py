string=str(input())
char1=str(input())
new=""
for i in string:
    if i==char1 and i not in new:
        new+=string.index(i)
        i='0'