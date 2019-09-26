s = "Hello World"
res = s[::-1]
print(res)

s1 = "Kartomin Petuh"

res1 = ""
for i in range(len(s1)-1, -1, -1):
    res1 = res1 + s1[i]
print(res1)
