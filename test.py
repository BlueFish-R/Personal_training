"""
1、编写函数实现topk查找，输入为整数数组与k，如[12,3,9,10,89,46,2,109,-1],k为5，输入[109,89,46,12,10
"""

def topk(k,list):
    list = sorted(list)[::-1]

    topk_list = list[-1:-1-k:-1]
    print(topk_list)

topk(5,[12,3,9,10,89,46,2,109,-1])

"""
2、使用一段代码实现对字符串的简单压缩，例如将‘abbccccddd’压缩为‘a1b2c4d3’，如果压缩后的字符串没有变短则返回原字符串
"""

str1 = "aabcde"
str2 = ""
head = str1[0]
num = 0
temp = False

for i in str1+"1":
    if i == head:
        num += 1
    elif i != head:
        str2 += str(head) + str(num)
        head = i
        num = 1

    if num > 1:
        temp = True

if temp:
    print(str2)
else:
    print(str1)