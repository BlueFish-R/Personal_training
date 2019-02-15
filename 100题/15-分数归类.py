'''
【程序15】
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
　　　60分以下的用C表示。
1.程序分析：(a>b)?a:b这是条件运算符的基本例子。
2.程序源代码：
不支持这个运算符
'''

grade = int(input("输入分数:\n"))

if grade >= 90:
    print("A")
elif grade >= 60 and grade < 90:
    print("B")
else:
    print("C")