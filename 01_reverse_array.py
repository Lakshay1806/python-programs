n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

for i in range(n // 2):
    temp = arr[i]
    arr[i] = arr[n - 1 - i]
    arr[n - 1 - i] = temp

print(arr)
