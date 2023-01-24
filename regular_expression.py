import re
value="This is a string"
output=re.search("^This.*string$",value) # ^ is starts with.....
#* is zero  or more occurences.
# . is any character
print(output)