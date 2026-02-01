n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input()))

if n == 1:
    print(0)
elif arr[0] == 0:
    print(-1)
else:
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        if i + arr[i] > farthest:
            farthest = i + arr[i]

        if i == current_end:
            jumps += 1
            current_end = farthest

            if current_end <= i:
                print(-1)
                break
    else:
        print(jumps)
