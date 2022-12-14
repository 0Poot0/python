def div(a,b):
    print(a/b)

def new_div(fun):
    def innerfun(a,b):
        if a<b:
            a,b=b,a
            return fun(a,b)
        return innerfun
    div=new_div(div)
div(3,4)