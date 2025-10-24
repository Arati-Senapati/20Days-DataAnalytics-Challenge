#Intrduction to  tuples
a =("apple","mango","banana",13,24)
print(a)
print(type(a))
b="kiwi"
print(b)
print(type(b))

#Slicing
a=("apple","mango","banana","kiwi")
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[::2])
print(a[::-1])
print(a[1::2])
print(a[2::-1])

#looping
#with for loop
for i in a:
    print(i)

#along with range and length in for loop
for i in range(len(a)):
    print(a[i])

#along with while loop
i=0
while i<len(a):
    print(a[i])
    i+=1

#conversion of tuples and tuple function
a = ("apple","mango","banana","kiwi")
print("before conversion",type(a))
a= list(a)
print("after conversion",type(a))
a.append("orange")
a=tuple(a)
print(type(a))
print(a)
