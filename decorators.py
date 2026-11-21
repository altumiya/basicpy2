# decorators is like toll booth
#A decorator adds extra functionality to a function without changing the original function's code.
# timing function execution
#args stores arguments without names, while kwargs stores arguments with names.
import time
def timer(func):
    def wrapper(*args, **kwargs): #wrapper is the function that controls what happens before and after the original function runs.
        start = time.time()
        result = func(*args, **kwargs) #Runs the original function
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time") #example_function ran in 2.0000813007354736 time
        return result
    return wrapper


@timer #this is decorator
def example_function(n):
    time.sleep(n)

example_function(2)

#debuging function call

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs. # k,v  is greeting salam
        items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}") # 1 calling: hello with args  and kwargs 
        return func(*args, **kwargs)
    
    return wrapper

@debug  #prints information about a function before executing it.
def hello():
    print("hello") # 2 hello

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}") # 3 calling: greet with args do u like to have coffee and kwargs greeting=salam  

hello()
greet("do u like to have coffee", greeting="salam ") # 4 salam , do u like to have coffee args = ("coffee",)
                                                       #kwargs = {"greeting": "salam"}

# How debugging works here:
# 1. @debug wraps the function inside wrapper, so calling hello() or greet() runs wrapper first.
# 2. wrapper captures and prints the function name, *args, and **kwargs so you can inspect the inputs.
# 3. After printing, it executes and returns the original function (func(*args, **kwargs)).

#cache return function
def cache(func):
    cache_value = {}
    print(cache_value) #{}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args] #It checks whether the arguments already exist as a key in the dictionary.
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 3)) #5
print(long_running_function(2, 3)) #5 this is cache refrence it does not calculate again
print(long_running_function(4, 3)) #7
# How caching works here:
# 1. cache_value = {} is created once when @cache decorates the function, storing past inputs (args) as keys and outputs as values.
# 2. First call (2, 3): not in cache_value, so it waits 4 seconds, computes 5, and saves {(2, 3): 5}.
# 3. Second call (2, 3): found in cache_value, so it skips time.sleep(4) and returns 5 instantly.
# 4. Call (4, 3): new input, so it waits 4 seconds and calculates 7 (only future calls with (4, 3) will be instant).
# Note: Make sure to add 'import time' at the top so time.sleep(4) works.