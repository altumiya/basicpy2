import math
m = 1
n = 2
o = 3
print(m==n<o) # cause and operator is use in internal working i.e. m==n  and n<o so false
print(m==n and n<o) #false
print(True==2) # also false

a = 3.5
print(math.floor(a)) # 3  roundoff closes lower value
print(math.floor(-3.5)) # -4 roundoff closes lower value
print(math.trunc(a)) # closest to 0
print(math.trunc(-3.5)) # -3 closest to 0

#ioata number
b = 2
c = 1j
print(b+c) #(2+1j)
print((2+1j)* 3) #(6+3j)