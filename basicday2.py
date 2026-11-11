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