import math

n = int(input())

bt = math.sqrt(2*n + 0.25) - 0.5
if bt - int(bt) == 0:
    bt -= 1
bt = int(bt)

s = bt + 2
p_sum = (bt + 1) * bt // 2 

if (bt + 1) % 2 == 0:
    numr = n - p_sum
    denom = s - numr
else:
    denom = n - p_sum
    numr = s - denom

print('{}/{}'.format(numr, denom))

