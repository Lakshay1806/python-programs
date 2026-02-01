n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

last = arr[n - 1]

for i in range(n - 1, 0, -1):
    arr[i] = arr[i - 1]

arr[0] = last

print(arr)
