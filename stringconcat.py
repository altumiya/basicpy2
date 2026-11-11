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