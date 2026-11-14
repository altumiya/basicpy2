# string '' "" ''' '''

seat = "sideupper"
print(seat[0]) # 1st character 's'
print(seat[0:4]) #side 
print(seat.upper()) # SIDEUPPER
print(seat.replace('upper', 'lower')) # replace upper to lower
print(seat) #og immutable
print(seat.find("upper")) # tell index 4
print(seat.find("Upper")) # index -1 as U is not present

