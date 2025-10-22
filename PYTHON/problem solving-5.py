a =["Ross","Rachel","Monica","Joe"]
#write a program to swap first and forth element.
a[0],a[3]=a[3],a[0]
print(a)

#write a program to add a new value at second position.
a.insert(1,"Phoebe")
print(a)
#write a program to delete a value from 3rd position.
a.pop(2)
print(a)

b=[13,7,12,10]
#write a program to multiply all the numbers in the list.
mul =1
for i in b:
    mul *= i
print(mul)

#write a program to get the largest number from the list.
b.sort()
print(b)
print("Largest value is",b[-1])
#write a program to get the smallest number from the list.
print("Smallest value is",b[0])