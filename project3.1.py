import re
#4 lower case character
#2 numbers
#1 symbol
#2 uppercase chaacter optional

mailid = re.compile("^[a-zA-Z0-1\.\_\]+@{1}[A-Za-z0-9]+\.{1}[a-zA-Z]{2,3}+$")
print(mailid.search("shrish23@gmail.com"))

password = re.compile("^[A-Z]{1,2}+[A-Za-z0-9]+[^a-zA-Z]{2,3}+$")
print(password.search("Shrish2@"))