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