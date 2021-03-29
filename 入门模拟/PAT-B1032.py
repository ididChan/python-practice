

n = int(input())

sum = []

for i in range(100000):
    sum.append(0)

for i in range(n):
    num, score = map(int, input().split())
    sum[num] += score

# sum = sum.tolist()
print(sum.index(max(sum)), int(max(sum)))
