#Introduction to Function
# def hello():
#     print("hello world")
# hello()
#
# def add():
#     x=56
#     y=23
#     print(x+y)
# add()

#parameters and arguments
# def add(a, b):
#     print(a + b)
#
#
# add(12, 67)
# add(12, 56)
#
#
# def rect(length, width):
#     print("area:", length * width)
#
#
# rect(12, 56)
#
#
# #arbitary argument
# def hello(*name):
#     print("Hello,my name is", name[2])
#
#
# hello("john", "lisa", "peter")
#
#
# #return statement
# def hello():
#     return ("hello world")


# print(hello())
#
# def add(a,b):
#     return ("addition:", a + b)
# print(add(12, 4))

#Recursion
# def hello():
#     print("hello")
#     return hello()
#
# print(hello())

# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n - 1)
#
# print(fact(5))

##Lambda function
# a=lambda b:b*5
# print(a(2))

# x = lambda a,b,c:(a+b)*c
# print(x(1,2,3))

##local and global variable
x=24
print("first variable is",x)
def hello():
    x=25
    return x
print(hello())
print("second variable is",x)

x=24
print("first variable is",x)
def hello():
    global x
    x=25
    return x
print(hello())
print("second variable is",x)