'''#Airthmetic Operator
print(12+5)
print(12-5)
print(12*5)
print(12/5)
print(12%5)
print(12//5)
print(12**5)

#Comparison Operator
print(3>2)
print(3>=2)
print(3==2)
print(3!=2)
print(3<2)
print(3<=2)

#Logical Operator
print(3>4 or 3<4)
print(not(3>4 or 3<4))
print(3>4 and 3<4)
print(not(3>4 and 3<4))

#Assignment Operator
x=6
print(x)
x=x+6
print(x)
x=x-6
print(x)
x=x*2
print(x)
x=x-2
print(x)

#Identity Operator
a=1234
b="1234"

print(a is b)
print(a is not b)

#Bitwise Operator
print(bin(10))

a=10
b=8
print(bin(a))
print(bin(b))
print(a&b)
print(a|b)
print(a^b)

print(a>>2)
print(a<<2)

#Membership Operator
a= "hello"
print("p" in a)
print("p" not in a)
print("e" in a)'''


#Conditional Statement

#if statement
marks=94
if marks >=90:
    print('u will get a mobile phone')

print("Thank u")

#if-else statement
marks=87
if marks >=90:
    print('u will get a mobile phone')
else:
    print('u will not get a mobile phone')
print("Thank u")

#if-elif-else statement
marks=50
if marks >=90:
    print("u can go for a trip")
elif marks >=80:
    print("u will get a mobile phone")
elif marks >=70:
    print("u will get a new book")
else:
    print("u will not get a mobile phone")
print("Thank u")

#nested if statement
marks=96
if marks >=90:
    print('u will get a mobile phone')
    if marks >=95:
        print('u will get a new book')
else:
    print('u will not get a mobile phone')
print("Thank u")

#shorthand if statement
marks=94
if marks >=90:print('u will get a mobile phone')

#shorthand if-else statement
marks=87
print('u will get a mobile phone') if marks >=90 else print('u will not get a mobile phone')