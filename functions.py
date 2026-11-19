
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