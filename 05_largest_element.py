n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print(largest)
