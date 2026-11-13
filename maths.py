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

print(0o20) #16  #octal number 
print(0xff) #255 hexal
print(0b1000) #8 binary

print(oct(64)) #0o100
print(hex(64)) #0x40
print(bin(64)) #0b1000000

print(int('64', 8)) #52
print(int('64', 16 )) #100
print(int('10000', 2))#16


# bit operator
x = 1
print(x<<2) # 4