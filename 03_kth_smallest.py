n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

k = int(input("Enter k: "))

for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(arr[k - 1])
