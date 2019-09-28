s = "Hello World"
res = s[::-1]
print(res)

s1 = "Kartomin Petuh"

res1 = ""
for i in range(len(s1)-1, -1, -1):
    res1 = res1 + s1[i]
print(res1)

s2 = ['hello', 'man', 'what', 'about', 'session exams?']
res2 = []
for i in range(len(s2)):
    res2.append(''.join(sorted(s2[i])))
print(res2)
