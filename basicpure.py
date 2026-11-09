print("hello world!")  #hello world string
print(10, type(10))  # int (Integer)
print(3.14, type(3.14))  # float (Floating point)
print(2 + 3j, type(2 + 3j))  # complex (Complex number)
print("Hello", type("Hello"))  # str (String)
print(True, type(True))  # bool (Boolean)
print(None, type(None))  # NoneType (None / Null)

# indentation example

def seat(n):
    print(n)

seat(4) #4
seat("hello world") #hello world
seat(float(3.14)) # 3.14

# from filename import function name above example 

# "seat" * 4 when run on shell it will give 'seatseatseatseat'

# mutable and immutable example

a = [1, 2, 3]
b = a

b.append(4)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3, 4]

a = [1, 2, 3]
b = a

b = [4, 5, 6]

print(a)  # [1, 2, 3]
print(b)  # [4, 5, 6]
# Initially, both variables referred to the same list. But when we assigned a new list to b, it started referring to a different object.

a = 10
b = a

b = 20

print(a)  # 10
print(b)  # 20
# Integers are immutable in Python.

#When you write b = 20, you aren't changing the integer 10 into 20. You're reassigning b to refer to the integer object  #representing 20.
