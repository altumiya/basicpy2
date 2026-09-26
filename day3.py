string1 = input("Enter a string: ")
string2 = input("Enter a string: ")
if len (string1) > len(string2):
    print(f"{string1} is greater than {string2}")
elif len(string1) < len(string2):
    print(f"{string1} is less than {string2}")
else:
    print(f"{string1} is equal to {string2}")