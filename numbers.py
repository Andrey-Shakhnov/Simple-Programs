print("Hello, enter any number")
num = int(input())

summ = 0
prod = 0

last = num % 10
first = num // 100
mid = (num // 10) % 10

print("First =", first, "Mid =", mid, "Last =", last)

summ = first + mid + last
prod = first*mid*last

print("Summ =", summ, "Product =", prod)
