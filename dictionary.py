#dictionaries are used to store data values in key value pair

myDictionary={
    "name": "Antara",
    "Class":12,
    "Rollno" :23,
    "age":18,
    #"age":22,
    #"percentage":30
}
#a=myDictionary.get("name")
#print(a)

#a=myDictionary.get("name")
#print(a)

#a=myDictionary.keys()
#print(a)

#a=myDictionary.values()
#print(a)

#a=myDictionary.items()
#print(a)

#myDictionary["age"]=19
#print(myDictionary)

#myDictionary.update({"age":22})
#print(myDictionary)

#myDictionary.pop("age")
#print(myDictionary)
#duplicates are not allowed

a=myDictionary.keys()
#print("The keys are :", a)

b=myDictionary.values()
#print("The values are:" , b)
#d=""
#for i in a:
 #   d+=i+","
#print("The keys are:", d)

myDictionary={
    "class":{
        "student":{
            "name":"abc",
            "marks":{
                "python":99,
                "web":30
            }
        }
    }
}
#print(myDictionary)

print(myDictionary["class"]["student"]["marks"]["web"])