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