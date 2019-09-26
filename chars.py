s = input("Enter string ")

count = 0
flag = 0

for i in range(len(s)):
    if s[i] != ' ' and flag == 0:
        count += 1
        flag = 1
    else:
        if s[i] == ' ':
            flag = 0

print(count)

s1 = input("Enter string s1 ")
s1 = s1.split()
l = len(s1)
print(l)
