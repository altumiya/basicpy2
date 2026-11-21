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

#inheritence

class Cars2:
    def __init__(self,userbrand, usermodel):
        self.brand = userbrand 
        self.model = usermodel 
    
    def fullName(self):
        return f"{self.brand} {self.model}"  
class ElectricV(Cars2):    
    def __init__(self,userbrand ,usermodel, batterySize):
        super().__init__(userbrand,usermodel)
        self.batterySize = batterySize
        
Ev = ElectricV("Tesla", "Model X" ,"300kw")     
print(Ev.fullName())   #Tesla Model X
myCars = Cars2("BMW" ,"I7")
print(myCars.fullName()) # BMW I7

# ENCAPSULATION and POLYMORPHISM
class Cars3:
    total_cars = 0

    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand  # [ENCAPSULATION] Private attribute (hidden using __)
        self.__model = usermodel  # [ENCAPSULATION] Private attribute (hidden using __)
        Cars3.total_cars += 1     # Class variable shared across all objects

    # [ENCAPSULATION] Getter: controlled read access to private __brand
    def get_brand(self):
        return self.__brand + " !"

    # [ENCAPSULATION] Setter: controlled write access to private __brand
    def set_brand(self, new_brand):
        self.__brand = new_brand

    def fullName(self):
        return f"{self.__brand} {self.model}"

    # [POLYMORPHISM] Base method (Petrol/Diesel version)
    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    # [ENCAPSULATION] @property: read-only access to private __model
    @property
    def model(self):
        return self.__model


class ElectricV(Cars3):
    def __init__(self, userbrand, usermodel, batterySize):
        super().__init__(userbrand, usermodel)
        self.batterySize = batterySize

    # [POLYMORPHISM] Method overriding: same method name, different behaviour for EVs
    def fuel_type(self):
        return "Electric charge"


mycars3 = Cars3("bmw", "i7")
print(mycars3.fuel_type())         # [POLYMORPHISM] Calls Cars3's fuel_type -> Petrol or Diesel

Ev = ElectricV("Tesla", "Model X", "300kw")
print(isinstance(Ev, Cars3))       # True (Inheritance)
print(isinstance(Ev, ElectricV))   # True (Inheritance)
print(Ev.fullName())

# print(Ev.__brand)                # [ENCAPSULATION] AttributeError: cannot access private variable directly
print(Ev.get_brand())              # [ENCAPSULATION] Reading private variable via getter -> Tesla !
Ev.set_brand("Rivian")             # [ENCAPSULATION] Modifying private variable via setter
print(Ev.get_brand())              # [ENCAPSULATION] -> Rivian !

print(Ev.fuel_type())              # [POLYMORPHISM] Calls ElectricV's fuel_type -> Electric charge

print(Cars3.total_cars)            # 2
print(mycars3.general_description())  # Cars are means of transport
print(mycars3.model)               # [ENCAPSULATION] Reading private __model via @property -> i7