#write a function to find maximum of three numbers in python.
def max_num(a,b,c):
    if a>b & a>c:
        print(a,"is greater number")
    elif b>c & a>b:
        print(b,"is greater number")
    else:
        print(c,"is greater number")
max_num(1,2,3)

#Write a python function to create and print a list where the values are square of numbers between 1 to 30
def create_list():
    l=[]
    for i in range(1,31):
       l.append(i**2)
    return l
print(create_list())

#write a python function that takes a number as a parameter and check if the number is prime or not.
def check_prime(num):
    if num == 1:
        print("it is not a prime number")
    if num == 2:
        print("it is a prime number")
    else:
        for i in range(2,num):
            if num%i==0:
                print("it is not a prime number")
                break
            else:
                print("it is a prime number")
check_prime(2)


#write a function to sum all the numbers in a list.
#solution 1
def add(numbers):
    total=0
    for i in numbers:
        total+=i
    return total
print(add([12,4,5,6,7,8]))

#solution 2
def sum(numbers):
    if len(numbers)==1:
        return(numbers[0])
    else:
        return((numbers[0])+sum(numbers[1:]))

print(sum([12,4,5,6,7,8]))

#write a python program to solve the fibonacci series along recursion
def fs(num):
    if num == 1:
        return(0)
    elif num == 2:
        return(1)
    else:
        return(fs(num-1)+fs(num-2))

print(fs(8))
