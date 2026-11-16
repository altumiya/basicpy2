#tuples are immutable 

seattypes = ("upper", "middle" ,"lower")
print(seattypes[1]) #middle
print(seattypes[-1]) #lower
#slicing and dicing also be done

moreseats = ("sidelower" ,"sideupper")
allseats = seattypes + moreseats
print(allseats) #('upper', 'middle', 'lower', 'sidelower', 'sideupper')
#The + operator creates a new tuple containing the items from both tuples:

if "middle" in allseats:
    print("seat present") # this runs
else:
    print("no such seats") 
print()

moreseats2 = ("sidelower" ,"sideupper" ,"sideupper")
print(moreseats2.count("sideupper")) #2 

seattypes2 = ("Upper", "Middle" ,"Lower")
(upper ,middle , lower) = seattypes2 # unpacks those values into three variables
print(upper) #Upper So upper gets "Upper", middle gets "Middle", and lower gets "Lower"