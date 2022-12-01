def something(a):
    return a*a

x=lambda a,b:a*b
num=x(5,2)
print(num)

def name(x,b):
    return lambda a:x/b

num=name(10,5)
print(num(2))