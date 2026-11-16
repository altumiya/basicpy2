# lists 
number = [1,2,3,4,5,6,7,8,9]
print(number[:])  #[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(number[3:8])  # [4, 5, 6, 7, 8]
print(number[:8]) # [1, 2, 3, 4, 5, 6, 7, 8]
print(number[0:7:2]) #[1, 3, 5, 7]
print(len(number)) #9

seatvar = ['upper' ,"middle" , '''lower''']
print(seatvar) 
print(seatvar[2]) #'lower'
print(seatvar[-2]) #middle
print(seatvar[1:2]) #['middle']
print(seatvar[:2]) #['upper', 'middle']

seatvar[2] = "sidelower"
print(seatvar) #['upper', 'middle', 'sidelower']

seatvar[1:2] = "sideupper"
print(seatvar) #['upper', 's', 'i', 'd', 'e', 'u', 'p', 'p', 'e', 'r', 'sidelower']

seatvar1 = ['upper' ,"middle" , '''lower''']
seatvar1[1:2] = ["sideupper"]
print(seatvar1) #['upper', 'sideupper', 'lower']
print(seatvar1[1:1]) #[]
seatvar1[1:1] = ["test", "test"]
print(seatvar1) #['upper', 'test', 'test', 'sideupper', 'lower']
seatvar1[1:3] = []
print(seatvar1) # remove items i.e test test so result is ['upper', 'sideupper', 'lower']
for seat in seatvar1:
    print(seat , end="-") # upper-sideupper-lower-
print()

   
seatvar1.append("sidelower")
print(seatvar1) #['upper', 'sideupper', 'lower', 'sidelower']
if "sidelowe" in seatvar1:
    print("sidelower is present") #if not present is shows nothing 
else:
    print("no such seats")    # this will run
print()    

seatvar1.pop()
print(seatvar1) #['upper', 'sideupper', 'lower']

seatvar1.remove("upper")
print(seatvar1) #['sideupper', 'lower']

seatvar1.insert(1,"upper")
print(seatvar1) #['sideupper', 'upper', 'lower']

#seatvar1.copy() creates a shallow copy—a new outer list in a different memory location—rather than a shared reference (=).

seatvar1_copy = seatvar1.copy()

seatvar1_copy.append('side-lower')

print(seatvar1)       # ['upper', 'middle', 'lower']              <- Untouched!
print(seatvar1_copy)  # ['upper', 'middle', 'lower', 'side-lower']
print(seatvar1 is seatvar1_copy)  # False (different objects in memory)

seatvar1_ref = seatvar1

seatvar1_ref.append('side-lower')

print(seatvar1)      # ['upper', 'middle', 'lower', 'side-lower']  <- Mutated!
print(seatvar1_ref)  # ['upper', 'middle', 'lower', 'side-lower']
print(seatvar1 is seatvar1_ref)  # True (same memory address)
