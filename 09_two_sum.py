n = int(input("Enter number of elements: "))

nums = []
for i in range(n):
    nums.append(int(input()))

target = int(input("Enter target: "))

for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == target:
            print([i, j])
            break
