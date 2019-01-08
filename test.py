str1 = "aabaa"

str2 = ""

head = ""

num = 0

for i in str1+'1':

    if num == 0:
        num += 1
        head = i

    elif i == head:
        num += 1

    elif i != head:
        str2 += str(head) + str(num)
        head = i
        num = 1

print(str2)
