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