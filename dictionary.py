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