#write a program to check if a number is positive.
number=int(input("enter a number:"))
if(number>0):
    print("Number is positive")

#write a program to check whether a number is odd or even.
number=int(input("enter a number:"))
if(number%2==0):
    print("Number is even")
else:
    print("Number is odd")

#write a program to create area calculator.
print("*****AREA CALCULATOR*****")
print("""press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of triangle
press 4 to get the area of circle""")

choice=int(input("enter your choice between 1 and 4:"))
if(choice==1):
    side=float(input("enter side of square:"))
    area=side*side
    print("The area of square is",area)
elif(choice==2):
    length=float(input("enter length of rectangle:"))
    breadth=float(input("enter breadth of rectangle:"))
    area=length*breadth
    print("The area of rectangle is",area)
elif(choice==3):
    height=float(input("enter height of triangle:"))
    base=float(input("enter base of triangle:"))
    area=0.5*height*base
    print("The area of triangle is",area)
elif(choice==4):
    radius=float(input("enter radius of circle:"))
    area=3.14*radius*radius
    print("The area of circle is",area)
else:
    print("please enter a valid choice")

#write a program to check whether the passed letter is a vowel or not.
letter=input("enter your letter:")
if (letter in 'aeiou') or (letter in 'AEIOU'):
    print("it is a vowel")
else:
    print("it is a consonant")

#write a program to check if a number is a single digit number,2-digit number and so on.. ,up to 5 digits.
number=int(input("enter your number:"))
if number>=0 and number<=10:
    print("it is a single digit number")
elif number>=10 and number<=100:
    print("it is a 2-digit number")
elif number>=100 and number<=1000:
    print("it is a 3-digit number")
elif number>=1000 and number<=10000:
    print("it is a 4-digit number")
else:
    print("it is a 5-digit number")