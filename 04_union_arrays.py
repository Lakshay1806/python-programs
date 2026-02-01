a = list(map(int, input("Enter elements of array A: ").split()))
b = list(map(int, input("Enter elements of array B: ").split()))

union = []

for num in a:
    if num not in union:
        union.append(num)

for num in b:
    if num not in union:
        union.append(num)

print(union)
