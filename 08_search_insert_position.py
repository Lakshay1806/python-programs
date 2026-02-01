n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter target: "))

low = 0
high = n - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print(low)
