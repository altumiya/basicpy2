#tuples are immutable 

seattypes = ("upper", "middle" ,"lower")
print(seattypes[1]) #middle
print(seattypes[-1]) #lower
#slicing and dicing also be done

moreseats = ("sidelower" ,"sideupper")
allseats = seattypes + moreseats
print(allseats) #('upper', 'middle', 'lower', 'sidelower', 'sideupper')
#The + operator creates a new tuple containing the items from both tuples: