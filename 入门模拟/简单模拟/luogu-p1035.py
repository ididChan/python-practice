k = int(input())
sum = 0
cnt = 0

while sum <= k:
    cnt += 1
    sum += 1 / cnt

print(cnt)