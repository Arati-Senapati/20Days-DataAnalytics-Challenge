#write a program to find a sum of all the even numbers up to 50.
# sum =0
# for i in range(0,51):
#     if i%2==0:
#         sum+=i
# print("Sum of all even number up to 50 is",sum)
from unittest import addModuleCleanup

#write a program to write 20 numbers and their squared numbers.
# for i in range(1,21):
#     print(i,"=",i*i)

#write a program to find sum of first 10 odd numbers using while loop.
# sum=0
# i=0
# while i<20:
#     if i%2!=0:
#         sum=sum+i
#     i+=1
# print("sum of first 10 odd numbers is",sum)

#write a program to check if a number is divisible by 8 and 12 up to 100 numbers.
# for i in range(1,100):
#     if i%8==0 and i%12==0:
#         print(i)

#write a program to create a billing system at supermarket.
while True:
    name=input("enter customer's name:")
    total=0
    while True:
        quantity=float(input("enter your quantity:"))
        amount=float(input("enter the amount:"))
        total+=quantity*amount
        repeat=input('do you want to add more items? (yes/no)')
        print("----------------------------------------")
        if repeat=='no' or repeat=='No':
            break
    print("Name:",name)
    print("Amount to be paid:",total)
    print("----------------------------------------")
    print("******Happy Customer******")
    repeat1=input("do you want to go to next customer?(yes/no) ")
    if repeat1=='no' or repeat1=='No':
        break

#pattern problem
for i in range (1,6):#rows
    for j in range (1,i+1):#columns
        print(j,end=" ")
    print()

for i in range (1,6):#rows
    for j in range (1,i+1):#columns
        print("*",end=" ")
    print()

for i in range (1,6):
    for j in range (6,i,-1):
        print(i,end=" ")
    print()

for i in range (1,6):
    for j in range (5,i,-1):
        print(" ",end=" ")
    for k in range (i):
        print("*",end=" ")
    print()

for i in range (1,6):
    for j in range (i,0,-1):
        print(j,end=" ")
    print()

for i in range (1,6):
    for j in range (1,i+1):
        print("*",end=" ")
    print()
for i in range (5,0,-1):
    for k in range (0,i-1):
        print("*",end=" ")
    print()

for i in range (1,11):
    for j in range (1,i+1):
        print(i*j,end=" ")
    print()


