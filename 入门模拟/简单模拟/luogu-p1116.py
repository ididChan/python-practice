n = int(input())
step = 0

arr = []
while len(arr)<n:
    num = input()
    nums = num.strip().split()
    nums = [int(i) for i in nums]
    for i in nums:
        arr.append(i)

for i in range(n-1):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            step += 1

print(step)