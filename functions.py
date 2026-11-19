
# functions defination

#basic syntex
import math
def square(number):
    print(number ** 2) #16  #inside () parameter is passed and variable is assigned
#square(4)  
result =  square(4)
print(result) #none so use return and arguement can be store in variable

def squ(num):
    return num ** 2
reslt = squ(5)
print(reslt)     # 25

# multiple parameters

def add(num1, num2):
    return num1 + num2
print(add(5,5))  #10
#print(5,5) give 55 and not error


#polymorphism
def multiply(p1,p2):
    return p1*p2
print(multiply(4,5))  #20
#print(4,5) give 45 no error
print(multiply('a', 5)) #aaaaa
print(multiply(5,'a')) #aaaaa

def circle(radius):
    area = (math.pi * radius ** 2)
    circum = (2 * math.pi * radius)
    return area , circum
a ,c = circle(4)  
print("area: {:.2f} circumference: {:.2f}".format(a, c))  #50.27, 25.13 last 2 digit only

# greeting default parameter

def greet(name = "user"):
    return "hello," + name + "!"
print(greet("altaf"))   #hello,altaf!
print(greet()) #hello,user!

# lambda or anonymous functions
# storing function in varialbe is called as lambda function

cube = lambda a:a**3
print(cube(4)) #64

#functions with *args  * allows a function to accept any number of positional arguments. class as tuples

def add_all(*args):
    print(f"Type: {type(args)}, Content: {args}")
    for i in args:
        print(i*2) #returns multiple values i.e. 2 4 6 8 10 15
    return sum(args)

# Call with 0, 2, or 5 arguments
print(add_all())              # Type: <class 'tuple'>, Content: () -> Returns 0
print(add_all(1, 2))          # Content: (1, 2) -> Returns 3
print(add_all(1, 2, 3, 4, 5)) # Content: (1, 2, 3, 4, 5) -> Returns 15

#function with **kwargs  ** allows a function to accept any number of named (keyword) arguments. in dictionary

def print_user_info(**kwargs): 
    print(f"Type: {type(kwargs)}") #Type: <class 'dict'>
    print(f"Dictionary content: {kwargs}") # Dictionary content: {'name': 'Altaf', 'role': 'Developer', 'city': 'Mumbai'}

    # Access just like a dictionary:
    for key, value in kwargs.items():
        print(f"  {key}: {value}")  #  name: Altaf role: Developer city: Mumbai

print_user_info(name="Altaf", role="Developer", city="Mumbai")

# generator function with yield method
def evengen(limit):
    for i in range(2, limit + 1, 2):
        yield i #yield pause execution of fn and save the  fn in local state
print(evengen(10)) #2 <generator object evengen at 0x6f75788de00> due to yield it will be random alphanumeric
for num in evengen(10):
    print(num) # 2 4 6 8 10

#recursive function  or exit function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial (4))  #24   

#scopes and closures or name space

username = "altumiya"

def func():
    username = "altaf"
    print(username)
print(username)    # altumiya due to global scope
func() #altaf after calling the function due to block scope

username1 = "altumiya"

def func1():
    #username1 = "altaf"
    print(username1)
print(username1)    # altimiya
func1() # altumiya as no var in innerscope the fn finding it on global scope