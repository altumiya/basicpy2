# dictonary key value pairs

seatdict ={"upper":"side" , "middle" : "exact", "lower" : "main"}
print(seatdict) #{'upper': 'side', 'middle': 'exact', 'lower': 'main'}
print(seatdict["middle"]) #exact
print(seatdict.get("lower")) #main
seatdict["upper"] = "sideupper"
print(seatdict) #{'upper': 'sideupper', 'middle': 'exact', 'lower': 'main'}
print(len(seatdict)) # 3 as three key-value pairs or 3 items are in dictonary 
for seat in seatdict:
    print(seat) #give keys
print()

for seat in seatdict:
    print(seat, seatdict[seat]) #give keys and their values
print()


for key, value in seatdict.items():
    print(key,value)   #give keys and their values
print()    

if "middle" in seatdict:
    print("seat present") # this runs
else:
    print("no such seats")    

seatdict["general"] = "sleeper"    
print(seatdict) #{'upper': 'sideupper', 'middle': 'exact', 'lower': 'main', 'general': 'sleeper'}

seatdict.pop("lower") #{'upper': 'sideupper', 'middle': 'exact', 'general': 'sleeper'} condition
 
print(seatdict)

seatdict.popitem()
print(seatdict) #{'upper': 'sideupper', 'middle': 'exact'} last item removed

del seatdict["middle"]
print(seatdict) #{'upper': 'sideupper'}

seattype ={
    "thirdac" : {"upper": "side" , "middle" : "exact", "lower" : "main"},
    "secondac" : {"upper": "side" , "lower" : "main"}
}
print(seattype) #{'thirdac': {'upper': 'side', 'middle': 'exact', 'lower': 'main'}, 'secondac': {'upper': 'side', 'lower': 'main'}}

print(seattype["secondac"]) #{'upper': 'side', 'lower': 'main'}
print(seattype["secondac"]["lower"]) #main

squnum = {x:x**2 for x in range(6)}
print(squnum) #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squnum.clear()
print(squnum)  # {}

print(squnum.clear()) #None