# 【题目描述】
# 第一行输入一个数，为n，第二行输入n个数，这n个数中，如果偶数比奇数多，输出NO，否则输出YES。
# 【输入】
# 输入有多组数据。
# 每组输入n，然后输入n个整数（1<=n<=1000）。
# 【输出】
# 如果偶数比奇数多，输出NO，否则输出YES。
###################################################
# 【样例输入】
# 1
# 67 
# 7
# 0 69 24 78 58 62 64 
# 【样例输出】
# YES
# NO

while True:
    try:
        n = int(input())
        arr = input()
        num = [int(i) for i in arr.split()]
        s = 0

        for i in range(n):
            if num[i] % 2 == 0:
                s += 1
            else:
                s -= 1
        
        if s > 0:
            print("NO")
        else:
            print("YES")

    except:
        break