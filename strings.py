# string '' "" ''' '''

seat = "sideupper"
print(seat[0]) # 1st character 's'
print(seat[0:4]) #side 
print(seat.upper()) # SIDEUPPER
print(seat.replace('upper', 'lower')) # replace upper to lower
print(seat) #og immutable
print(seat.find("upper")) # tell index 4
print(seat.find("Upper")) # index -1 as U is not present

seat2 = '   sidelower   '
print(seat2.strip())  # space stipped off

seat3 = "upper , lower , middle, sideupper, sidelower"
print(seat3.split(", ")) # from string to list ['upper ', 'lower ', 'middle', 'sideupper', 'sidelower']

# formatting
seatname = "sidelower"
seatno = 34
order = "i booked seat number {} which is {}" 
print(order.format(seatno, seatname)) # i booked seat number 34 which is sidelower
print("lower" in seatname) #True

seatvar = ["lower" ,"upper", "middle"]
print(", ".join(seatvar)) #lower, upper, middle 

seatfun = "sideupper and sidelower"
for letter in seatfun:
  print(letter) # give every letter

seatqu = "he said \"sidelower is best seat\""
print(seatqu) #he said "sidelower is best seat"

seatweb = r"www.seatbook.com/booking/select"
print(seatweb) #if r is not given then it shows error