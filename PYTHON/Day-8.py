#Intoduction to Modules
#In-built modules
#Datetime modules
# import datetime
# x=datetime.datetime.now()
# print(x)
#
# y=datetime.datetime(1997,10,14)
# print(y.strftime("%A"))
# print(y.strftime("%a"))
# print(y.strftime("%B"))
# print(y.strftime("%b"))
# print(y.strftime("%m"))
# print(y.strftime("%Y"))
# print(y.strftime("%y"))
# print(y.strftime("%d"))
# print(y.strftime("%w"))
# print(y.strftime("%H"))
# print(y.strftime("%I"))
# print(y.strftime("%M"))
# print(y.strftime("%S"))
# print(y.strftime("%p"))

#Random modules
# import random
# x= random.randint(1,10)
# print(x)
#
# l=["HEADS","TAILS"]
# print(random.choice(l))

#Math modules
# import math
# x=max(13,67,45)
# print("The maximum value is",x)
# x=min(13,67,45)
# print("The minimum value is",x)
# a=pow(2,4)
# print(a)
# b=math.sqrt(49)
# print(b)
# c=abs(-12.345)
# print(c)
# print(math.ceil(2.4))
# print(math.floor(2.4))

#Creation of modules
import demo
a=demo.add(2,3)
print(a)

import demo as d
a=d.add(5,6)
print(a)

b= d.employee["Name"]
print(b)





