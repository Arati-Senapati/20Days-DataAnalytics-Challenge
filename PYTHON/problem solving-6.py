#convert the following dictionary into json format.
# import json
# Student_data={"name":"David","age":13,"marks":87}
# print(type(Student_data))
# data= json.dumps(Student_data)
# print(data)
# print(type(data))
#access the value of age from the given data.
import json
# Student_data="""{"name":"David","age":13,"marks":87}"""
# data = json.loads(Student_data)
# print(data["age"])
#pretty print following json data.
# Student_data={"name":"David","age":13,"marks":87}
# data = json.dumps(Student_data,indent=4,separators=(",","="))
# print(data)
#sort the following json keys and write them into a file.
# Student_data={"name":"David","age":13,"marks":87}
# f=open("demo.json","w")
# data = json.dumps(Student_data,indent=4,sort_keys=True)
# f.write(data)
# print("thr data has been added to the file")


#access the nested key marks from the following nested data
# student_data ="""{"student":{
#     "grade":{
#     "name":"David",
#     "marks":{
#     "math":87,}
#     }
# }"""
#
# data = json.loads(student_data)
# print(data["student"]["grade"]["name"]["marks"])


##Dictionary problem solving
#write a python program to sort a dictionary by value.
# data = {"a":26,"b":100,"c":98,"d":45}
# data = sorted (data.values())
# print(data)
#
# #write a python script to print a dictionary where the keys are number between 1 and 15 and the values are square of keys.
# a={}
# for i in range (1,16):
#     a[i]=i**2
# print(a)
#
# #write a pyhon program to multiply all the items in a dictionary.
# a ={"a":1,"b":2,"c":3,"d":4,"e":5}
# product =1
# for i in a:
#     product*=a[i]
# print(product)
#
# #write a python program to sort a dictionary by key.
# data = {12:"a",56:"b",23:"c"}
# print(data)
# a = sorted(data.keys())
# print(a)

##sets problem solving
#write a program to find max and min in a set.
a={12,56,34,8,90,1,57}
print("min value:", min(a))
print("max value:", max(a))

#write a program to find common elements in three lists using sets.
a=[1,5,6,8,2]
b=[4,5,6,7]
c=[1,9,6,2,5]
print(set(a)&set(b)&set(c))

#write a program to find difference between two sets.
a={1,5,6,8,2}
b={4,5,6,7}
print(a.difference(b))

#write a program to remove an item from a set if it is present in the set.
a={1,5,6,8,2}
a.discard(8)
print(a)

#write a program to check if a set is  a subset of another set.
a={1,5,6,8,2}
b={5,6}
print(b.issubset(a))
print(a.issubset(b))













