def list(names):
    for i in names:
        length=len(i)
        if len>5:
            return i
names=["Atul","Shubham","Anurag","rahul","dev","roy"]
ans=list(names)
print(ans)