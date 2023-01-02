#try:
    #this block of code will run and throw errors if there are any
#except:
    #this will raise errors
#else:
    #this will execute if there are no errors.
#finally:
#this will execute regardless the code result of try and except
try:
    f=open("demo.py")
    try:
        f.write("ABC")
    except:
        print("Error in file")
    finally:
        f.close()
except:
    print("can't open the file")

    