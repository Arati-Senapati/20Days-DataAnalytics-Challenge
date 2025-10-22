#Introduction to lists
fruits = ["apple", "orange", "banana",12,13,14]
print(fruits)
print(type(fruits))

#slicing list
a=["Ironman","Thor","Captain America","Hulk"]
print(a[-1])
print(a[1:3])
print(a[:2])
print(a[1:])
print(a[::2])
print(a[-3:-1])

print(a[::-1])
print(a[-1:-4:-1])

#list iteration -4types
# Iteration using For Loop
a=["Ironman","Thor","Captain America","Hulk"]
for i in a:
    print(i)

#Iteration using For Loop with range and length function
a=["Ironman","Thor","Captain America","Hulk"]
for i in range(len(a)):
    print(a[i])

#Iteration using While Loop
a=["Ironman","Thor","Captain America","Hulk"]
i=0
while i<len(a):
    print(a[i])
    i+=1

#using short hand for loop
a=["Ironman","Thor","Captain America","Hulk"]
[print (i) for i in a]
[print (a[i] ) for i in range(len(a))]

#List Function
a=["Ironman","Thor","Captain America","Hulk"]

#to find the length of a list
print(len(a))
#to count and occurence of a particular element
print(a.count("Hulk"))
#to add to the list
a.append("Spiderman")
print(a)
#to add to a specific location
a.insert(1,"Vision")
a.insert(-2,"Batman")
print(a)
#to remove from a list
a.remove("Hulk")
print(a)
#to remove from a certain location
print(a.pop(1))
print(a)
#to create a copy of a list
b= a.copy()
print(b)
#to access an element
print(a.index("Ironman"))
#to extend the list
c=["Vision","Hulk"]
a.extend(c)
print(a)
#to reverse the list
a.reverse()
print(a)
#to sort the list
a.sort()
print(a)
#to clear all the data from the list
a.clear()
print(a)
c.clear()
print(c)

#list comprehension
l1=[30,40,50,60]
l2=[]
for i in l1:
    if i > 45:
        l2.append(i)
print(l1,"\n",l2)

l3 =[i for i in l1]
print(l3)
l3 =[i for i in l1 if i > 45]
print(l3)