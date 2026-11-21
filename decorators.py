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