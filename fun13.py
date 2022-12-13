#arbitary keyword argument
def info(name,**data):
    print(name)
    for i,j in data.items():
        print(i,j)

info("Antara", age=18, place="Agartala",num=99999999)