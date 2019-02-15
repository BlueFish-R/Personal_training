'''
【程序14】
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,
　重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

2.程序源代码：
'''
num = int(input("请输入一个数:"))
num1 = num
l = []
i = 2
while 1:
    if num1 == i:
        print("%d=%d"%(num,i))
        continue
    elif num1 % i == 0:
        l.append(i)
        num1 /= i
    elif num1 % i != 0:
        i += 1
    if num1 == 2 or num1 == 3 or num1 == 5:
        print("%d="%num1,end='')
        for a in l:
            print("%d*"%a)
        break


