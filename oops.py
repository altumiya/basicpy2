# oops in python
#class is blueprint to creat object
class Cars:   #name of class
    def __init__(self,userbrand, usermodel): #__init__() is a special method that Python calls automatically when an object is initialized and also called as constructor
        self.brand = userbrand #self refers to the particular object whose method is being called.
        self.model = usermodel  #self.var means class variables and uservar is parameters by users

car1 = Cars("Honda", "Elevate")
car2 = Cars("Toyota", "Fortuner")
car3 = Cars("Tata", "Nexon")
        
print(car1.brand) #Honda
print(car2.model) #Fortuner
print(car3.brand,car3.model) # Tata Nexon
print(car3) #<__main__.Cars object at 0xab205146ba0>

#class method and self

class Cars1:
    def __init__(self,userbrand, usermodel):
        self.brand = userbrand 
        self.model = usermodel 
    
    def fullName(self):
        return f"{self.brand} {self.model}"    
myCars = Cars1("BMW" ,"I7")
print(myCars.fullName()) # BMW I7