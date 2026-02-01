n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

max_sum = arr[0]
current_sum = 0

for num in arr:
    current_sum = current_sum + num

    if current_sum > max_sum:
        max_sum = current_sum

    if current_sum < 0:
        current_sum = 0

print(max_sum)
