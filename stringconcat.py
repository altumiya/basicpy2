#operation overloading or concatanation

a= 'altaf'
b = 'altumiya'
print(a+b) #altafalumiya

a1 = "altumiya"

print(a1) #altumiya
print(repr(a1)) # 'altumiya' returns a string representation that shows the quotes around the original string.

a2 = "Hello\nWorld"  #\n represents a newline character.

print(a2) # hello  world
print(repr(a2)) # '"Hello\nWorld"'  This makes repr() useful for debugging.

a3 = "hello\nworld"

print(str(a3))  # hello # world
print(repr(a3)) #hello\world

a4 = "123"

print(a4) # 123
print(repr(a4)) # '123'
print(type(a4)) # <class 'str'>
print(type(repr(a4))) # <class 'str'>