'''
【程序17】
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
1.程序分析：利用while语句,条件为输入的字符不为'\n'.
　　　　　　
2.程序源代码：
'''
str_list = str(input("请输入一行字符串："))
dict = {}
for i in str_list:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)