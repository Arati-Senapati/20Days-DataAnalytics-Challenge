#string manipulation
# a="why fit in, When you are born to stand Out!"
# print(len(a))
# print(a.count("o"))
# print(a.upper())
# print(a.lower())
# print(a.index("o",25,43))
# print(a.title())
# print(a.casefold())
# print(a.capitalize())
# print(a.find("s",25,43))
# print(a.find("o",25,43))
#
# name="arati"
# age=24
# a="my name is ",name
# print(a)
# b="my name is {} and my age is {}"
# print(b.format(name,age))
#
# print(name.center(20,"*"))

#string function
# a="hello"
# b="Hello123"
# c="123456"
# d="HELLO"
# e=" "
# f="Hello 123"
# g="1.234"
# h="hello123"
# i="Harry Potter And The Goblet Of Fire"
# j="Hello everyone"

#isalnum - Returns True if all characters in the string are alphanumeric
# print(a,a.isalnum())
# print(b,b.isalnum())
# print(c,c.isalnum())
# print(f,f.isalnum())
# print(g,g.isalnum())
#
# #isalpha - Returns True if all characters in the string are alphabet
# print(a,a.isalpha())
# print(b,b.isalpha())
#
#
# #isdecimal - Returns True if all characters in the string are decimals
# print(a,a.isdecimal())
# print(b,b.isdecimal())
# print(g,g.isdecimal())
# print(c,c.isdecimal())
#
# #isdigit - Returns True if all characters in the string are digits
# print(a,a.isdigit())
# print(c,c.isdigit())
# print(f,f.isdigit())
# print(g,g.isdigit())
#
# #isnumeric - Returns True if all characters in the string are numeric
# print(b,b.isnumeric())
# print(c,c.isnumeric())
# print(e,e.isnumeric())
#
# #islower - check if the string is lower case or not
# print(a,a.islower())
# print(d,d.islower())
# print(b,b.islower())
# print(h,h.islower())
#
# #isupper - check if the string is upper case or not
# print(a,a.isupper())
# print(d,d.isupper())
# print(b,b.isupper())
#
# #isspace - returns true if all character in the string are whitespaces
# print(e,e.isspace())
# print(f,f.isspace())
#
# #istitle - returns true if the string follows the rule of a title
# print(b,b.istitle())
# print(i,i.istitle())
# print(j,j.istitle())
#
# #endswith() - returns true if the string ends with the specified value
# a="Harry Potter"
# print(a.endswith("r"))
# print(a.endswith("t",6,9))
#
# #startswith() - returns true if the string starts with the specified value
# a="Harry Potter"
# print(a.startswith("H"))
# print(a.startswith("P",6,9))
#
# #swapcase() - swaps cases,lower case becomes upper case and vice versa
# a="Harry Potter"
# print(a.swapcase())

#strip() - returns a trimmed version of the string
# b="   Harry Potter    "
# a="*****Harry Potter......"
# print(b)
# print(a)
# print(a.strip("*,., "))
# print(b.strip())
#
# #split() - splits the string at the specified separator, and returns a list
# a = "#OOFD#BRB#OMW#TB"
# print(a.split('#'))
# b="hello. my name is john. iam 23 years old"
# print(b.split("."))
#
# #ljust() - returns a left justified version of the string
# a="Harry Potter"
# x = a.ljust(10)
# y= a.ljust(20,"*")
# print(x, "is my favorite movie")
# print(y, "is my favorite movie")
#
# #rjust() - returns a right justified version of the string
# a="Harry Potter"
# x = a.rjust(10)
# y= a.rjust(20,"*")
# print(x, " is my favorite movie")
# print(y, " is my favorite movie")
#
# #replace() - returns a string where a specified value is replaced with a specified value
# a="my name is john"
# print(a)
# print(a.replace("john","harry"))
#
# #rindex() - searches the string for a specified value and returns the last position of where it was found
# a= "Harry Potter and the prisoner of azkaban"
# print(a.rindex("prisoner"))
# print(a.rindex("azkaban"))
#
# #rfind() - searches the string for a specified value and returns the last position of where it was found
# a= "Harry Potter and the prisoner of azkaban"
# print(a.find("Harry"))
# b="bibidy bobidy boo"
# print(a.rfind("dy",6,14))

#Slicing in Strings
a="Harry Potter and the University of Nottingham"
print(a)
print(a[0:5])
print(a[6:12])
print(a[:12])
print(a[-4:])

b="0123456789"
print(b[::2])
print(b[:7:2])
print(b[::-1])
print(b[6::-1])