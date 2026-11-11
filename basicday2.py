arr1 = [2, 3, 4, 2, 3]

seen = set()
repeated = set()

for value in arr1:
    if value in seen:
        repeated.add(value)
    else:
        seen.add(value)

print(sorted(repeated))  # [2, 3]
print(sorted(seen)) #[2, 3, 4]

arr12 = [2, 3, 4, 2, 3]

unique = 0

for i in range(len(arr1)):
    unique = unique ^ arr12[i]

print(unique)  # 4

# slicing copy refer
import copy
h1 = [1,2,3]
h2 = h1[:] # slicing make copy and then refer 
h1[0]= 55
print(h1) #[55, 2, 3]
print(h2) #[1, 2, 3]

h2 = copy.copy(h1)  #copy.deepcopy for nested list
print(h2) #[55,2,3]

# is example

m = [1,2,3]
n = m
print(m) # [1,2,3]
print(n) # [1,2,3]
print( m == n) #true
m = [1,2,3]
print(m is n) #False as is compares identity