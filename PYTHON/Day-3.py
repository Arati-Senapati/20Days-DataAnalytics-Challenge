# #for-Loops
# for i in range(1,6):
#     print("hello world")
#
# for i in range(1,6,2):
#     print(i)
#
# n=int(input("enter a number:"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)
from itertools import repeat

#while-loop
# n=0
# while n<=5:
#     print(n)
#     n+=1
#
# n=1
# a=int(input('enter a number here: '))
# while n<=10:
#     print(a,"*",n,"=",a*n)
#     n+=1

#while-true
# n=1
# while True:
#     print(n)
#     n+=1

# while True:
#     num1=int(input("Enter a number"))
#     num2=int(input("Enter another number"))
#
#     print(num1+num2)
#     repeat = input("Do you want to repeat? (y/n)")
#     if repeat == "y":
#         break

#nested-loops
# for i in range(1,4):
#     for j in range(1,11):
#         print(j, end="")
#     print()
#
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end =" " )
#     print()

#for loop with conditional statement
# for i in range(1,11):
#     if i==3:
#         print("add this song to the favs")
#     else:
#         print(i)
#
# for i in range(1,101):
#     if i%8==0 and i%12==0:
#         print(i)
#
# n=1
# while n<=10:
#     if n==3:
#         print("add this to favs")
#     else:
#         print(n)
#     n=n+1

#break and continue statement
for i in range(1,11):
    if i==3:
        continue
    else:
        print(i)

for i in range(1,11):
    if i==3:
        break
    else:
        print(i)
print("thank you")