n1 = int(input("Enter number of elements in A: "))
a = []
for i in range(n1):
    a.append(int(input()))

n2 = int(input("Enter number of elements in B: "))
b = []
for i in range(n2):
    b.append(int(input()))

union = []

for num in a:
    if num not in union:
        union.append(num)

for num in b:
    if num not in union:
        union.append(num)

print(union)

