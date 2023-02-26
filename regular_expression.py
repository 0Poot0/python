import re
value="This is a string"
output=re.search("^This.*string$",value)  # ^ is starts with.....
print(output)
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+=-])(?=.{8,})"

# []	A set of characters
# \	Signals a special sequence (can also be used to escape special characters
# .	Any character (except newline character
# ^	Starts with	
# $	Ends with	
# *	Zero or more occurrences	
# +	One or more occurrences	
# ?	Zero or one occurrences
# {}	Exactly the specified number of occurrences
# |	Either or
# ()	Capture and group
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case
# /s : matches any whitespace characters such as space and tab
# /S : matches any non-whitespace characters
# /d : matches any digit character
# /D : matches any non-digit characters
# /w : matches any word character (basically alpha-numeric)
# /W : matches any non-word character
# /b : matches any word boundary (this would include spaces, dashes, commas, semi-colons, etc)
# @ at symbol