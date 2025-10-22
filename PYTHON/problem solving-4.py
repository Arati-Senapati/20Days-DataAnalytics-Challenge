# #String problem
# A="why fit in, When you are born to stand Out!"
# #write a program to find the length of the following string.
# print(len(A))
# #write a program to check how many times alphabet o is occurring.
# print(A.count("o"))
# #write a program to convert the whole string into lower and upper case.
# b=A.lower()
# print(b)
# c=A.upper()
# print(c)
# #write a program to convert the following string into a title.
# d=A.title()
# print(d)
# #write a program to find the index number of "fit in".
# print(A.find("fit in"))


#write a program to Fibonacci series up to 10 numbers.
# a = 0
# b = 1
# n = int(input("enter a number here:"))
# if(n==1):
#     print(1)
# else:
#     print(a)
#     print(b)
#     for i in range(2,n):
#         c = a+ b
#         a=b
#         b=c
#         print(c)
#write a program to check if a number is prime or not.
# num = int(input("enter a number here:"))
# if num<=1:
#     print("it is not a prime number")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("it is not a prime number")
#             break
#     else:
#         print("it is a prime number")


#write a program to find a palindrome of integers.
# num = int(input("enter your number: "))
# temp = num
# rev=0
# while num>0:
#     digit = num%10
#     rev=rev*10+digit
#     num=num//10
# if rev==temp:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")


#write a program to create an area calculator.
# print("*****AREA CALCULATOR*****")
# while True:
#     print("""press 1 to get the area of square
#     press 2 to get the area of rectangle
#     press 3 to get the area of triangle
#     press 4 to get the area of circle""")
#
#     choice=int(input("enter your choice between 1 and 4:"))
#     if(choice==1):
#         while(True):
#             side=float(input("enter side of square:"))
#             area=side*side
#             print("The area of square is",area)
#             repeat = input("do you want to try again with square?(yes/no) ")
#             if repeat=='no' or repeat=='No':
#                 break
#     elif(choice==2):
#         while(True):
#             length=float(input("enter length of rectangle:"))
#             breadth=float(input("enter breadth of rectangle:"))
#             area=length*breadth
#             print("The area of rectangle is",area)
#             repeat = input("do you want to try again with rectangle?(yes/no) ")
#             if repeat == 'no' or repeat == 'No':
#                 break
#     elif(choice==3):
#         while(True):
#             height=float(input("enter height of triangle:"))
#             base=float(input("enter base of triangle:"))
#             area=0.5*height*base
#             print("The area of triangle is",area)
#             repeat = input("do you want to try again with triangle?(yes/no) ")
#             if repeat == 'no' or repeat == 'No':
#                 break
#     elif(choice==4):
#         while(True):
#             radius=float(input("enter radius of circle:"))
#             area=3.14*radius*radius
#             print("The area of circle is",area)
#             repeat = input("do you want to try again with square?(yes/no) ")
#             if repeat == 'no' or repeat == 'No':
#                 break
#     # else:
#     #     print("please enter a valid choice")
#     repeat1 = input("do you want to repeat the menu again?(yes/no) ")
#     if repeat1 == 'no' or repeat1 == 'No':
#         break

# a="OOTD.YOLO.ASAP.BRB.GTG.OTW"
# #write a program to separate the following string into coma(,) separated value.
# print(a.split("."))
# #write a program to sort strings alphabetically in python.
# b="hello"
# print(sorted(b))
# #write a program to remove a given character from a string.
# c="hello"
# print(c.replace("e",""))
# Z="F.R.I.E.N.D.S."
# #write a program dot(.) from the following string.
# print(Z.replace(".",""))
# #write a program to check the number of occurence
# a="she sells seashells on the seashore of foreign currencies"
# print(a.count("sea"))

#take an input from user as a string then,reverse it.
c= (input("Enter a string: "))
print(str[::-1])

#write a program to check if a string contains only digits.
a= (input("Enter a string: "))
b=(a.isdigit())
if b == True:
    print("contain only digits")
else:
    print("does not contain only digits")

#write a program to check if a string is palindrome.
a=input("Enter a string: ")
rev = a[::-1]
print(rev)
if a == rev:
    print("Yes, the string is a palindrome")
else:
    print("No, the string is not a palindrome")

#write a program to find number of vowels in a string.
a=input("Enter a string: ")
vowels=0
for i in a:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        vowels+=1

print("Number of vowels: ",vowels)

#write a program to check if every word in a string begins with a capital letter.
a=input("Enter a string: ")
print(a.istitle())
