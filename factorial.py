n = int(input("enter any value "))

res = 1
for i in range(1, n+1, 1):
    res *= i
print(res)

N = int(input("Enter N "))


def fact(N):
    if N == 0:
        return 1
    return fact(N-1)*N

res2 = fact(N)
print(res2)
