n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

minimum = arr[0]
maximum = arr[0]

for num in arr:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print([minimum, maximum])

