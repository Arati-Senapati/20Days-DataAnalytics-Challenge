#Intrduction to  tuples
# a =("apple","mango","banana",13,24)
# print(a)
# print(type(a))
# b="kiwi"
# print(b)
# print(type(b))
#
# #Slicing
# a=("apple","mango","banana","kiwi")
# print(a[1:3])
# print(a[:3])
# print(a[2:])
# print(a[::2])
# print(a[::-1])
# print(a[1::2])
# print(a[2::-1])
#
# #looping
# #with for loop
# for i in a:
#     print(i)
#
# #along with range and length in for loop
# for i in range(len(a)):
#     print(a[i])
#
# #along with while loop
# i=0
# while i<len(a):
#     print(a[i])
#     i+=1
#
# #conversion of tuples and tuple function
# a = ("apple","mango","banana","kiwi")
# print("before conversion",type(a))
# a= list(a)
# print("after conversion",type(a))
# a.append("orange")
# a=tuple(a)
# print(type(a))
# print(a)

#Introduction to Dictionary
# Employee_Data = {
#     "name":"John",
#     "age":22,
#     "gender":"male",
# }
# print(Employee_Data)
# print(Employee_Data["name"])
# print(Employee_Data["age"])
# print(Employee_Data["gender"])
#
# #Iteration in dictionary
# Employee_Data = {
#     "name":"John",
#     "age":22,
#     "gender":"male",
# }
# #printing all key names one by one:
# for key in Employee_Data:
#     print(key)
#
# #printing all key names one by one:
# for key in Employee_Data:
#     print(Employee_Data[key])
#
# #using value function
# for key in Employee_Data.values():
#     print(key)
#
# #using items function
# for key,value in Employee_Data.items():
#     print(key,":",value)

#dictionary function
# Student_Data = {
#     "name":"John",
#     "age":22,
#     "gender":"male",
# }
#
# #get -returns the value
# x =Student_Data.get("name")
# print(x)
# print(Student_Data.get("age"))
# print(Student_Data.get("gender"))
#
# #item
# a = Student_Data.items()
# print(a)
#
# #keys
# b = Student_Data.keys()
# print(b)
#
# #values
# c = Student_Data.values()
# print(c)
#
# #copy
# d = Student_Data.copy()
# print(d)
#
# #setdefault
# x = Student_Data.setdefault("marks",98)
# print(x)
# print(Student_Data)
#
# #update
# x = Student_Data.update({"name":"arati"})
# print(Student_Data)
#
# #pop
# Student_Data.pop("marks")
# print(Student_Data)
#
# #popitem
# Student_Data.popitem()
# print(Student_Data)
#
# #clear
# Student_Data.clear()
# print(Student_Data)
#
# #Nested Dictionaries
# Employee_Data = {1:{"name": "John","age": 22,"gender": "male"},
#                  2:{"name": "Radha","age": 23,"gender": "female"},
#                  3:{"name": "Ram","age": 24,"gender": "male"}}
# print(Employee_Data)
# print(Employee_Data[2]["gender"])
# print(Employee_Data[1]["gender"])
# print(Employee_Data[1])

##Introduction to sets
# a ={"apple","mango","banana",34,56}
# print(a)
# print(type(a))
# for x in a:
#     print(x)
#
# #set function-
# #add
# a.add("orange")
# print(a)
#
# #pop
# print(a.pop())
# print(a)
#
# #remove
# a.remove("orange")
# print(a)
#
# #discard
# a.discard("apple")
# print(a)
#
# #copy
# b=a.copy()
# print(b)

a ={"ironman","hulk","thor","captain america"}
b ={"Superman","batman","wonder-woman"}
c={"hulk","thor"}
#isdisjoint
# print (a.isdisjoint(b))
# print (a.isdisjoint(c))
#
# #issubset
# print (a.issubset(b))
# print (c.issubset(a))
#
# #issuperset
# print(b.issuperset(a))
# print(a.issuperset(c))
#
# #update
# a.update(b)
# print(a)
# a.update(c)
# print(a)
#
# #clear
# a.clear()
# print(a)

#union
# print(a.union(b))
# print(b.union(c))
#
# #difference
# print(a.difference(b))
# print(b.difference(c))
# print(a.difference(c))

#difference_update
# a.difference_update(c)
# print(a)

#intersection
# print(a.intersection(c))

#intersection_update
# a.intersection_update(c)
# print(a)

#symmetric difference
x=a.symmetric_difference(c)
print(x)
y=b.symmetric_difference(c)
print(y)

#symmetric_difference_update
a.symmetric_difference_update(c)
print(a)