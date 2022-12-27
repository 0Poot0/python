# f= open("demo.txt","r",encoding="utf-8")
# #print(f.read())
# #print(f.readline())
# #print(f.readline())

# #f1=open("demo1.txt","w"
# f2=open("demo2.txt","w")

# f2.write("My name is Antara...\n")
# f2.write("I am Antara...")

# for i in f:
#     f2.write(i)
# try:
#     f=open("demo.txt")
# #f=open("demo.txt")
# finally:
#     f.close()
    #This way we are making sure that the file is closed properly even if exception is raised that cause thr program flow to stop....

# f=open("demo.txt","r")
# print(f.read(10))
# print(f.tell())

f=open("pic11.jpg","rb")
print(f.read())