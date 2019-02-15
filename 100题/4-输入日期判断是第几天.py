'''题目：输入某年某月某日，判断这一天是这一年的第几天？
1.程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊
　　　　　　情况，闰年且输入月份大于3时需考虑多加一天。
2.程序源代码：
'''
year = int(input("请输入年：\n"))
month = int(input("请输入月：\n"))
day = int(input("请输入日：\n"))
day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sum = 0

for i in day_list[:month-1]:
    sum += i

if year % 4 == 0 or year % 100 == 0:
    if month > 2 :
        sum += day + 1
    else:
        sum += day

print(sum)


