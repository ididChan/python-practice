# 【题目描述】
# 写个算法，对2个小于1000000000的输入，求结果。特殊乘法举例：123 * 45 = 1*4 +1*5 +2*4 +2*5 +3*4+3*5
# 【输入】
# 两个小于1000000000的数
# 【输出】
# 输入可能有多组数据，对于每一组数据，输出Input中的两个数按照题目要求的方法进行运算后得到的结果。
########################################################################################
# 【样例输入】
# 24 65
# 42 66666
# 3 67
# 【样例输出】
# 66
# 180
# 39

while True:
    try:
        num = input().split()
        s = 0

        for ch in num[0]:
            ch = int(ch)
            for cch in num[1]:
                cch = int(cch)
                s += ch * cch
        
        print(s)

    except:
        break