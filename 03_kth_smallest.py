arr = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter k: "))

n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(arr[k - 1])
