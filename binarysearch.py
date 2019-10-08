from random import randint

a = []
n = int(input("Enter size of list: "))

if n >= 10:
	a = [randint(0,100) for i in range(n)]
else:
	for i in range(n):
		a.append(int(input("Enter elements: ")))
a = sorted(a)
print(a)

key = int(input("Enter'Key': "))

def bin(a,key):
	mid = n // 2
	first = 0
	last = n-1
	print("Start mid ",a[mid])
	while (a[mid] != key and first <= last):
		if (key > a[mid]):
			first = mid + 1
		else:
			last = mid - 1
		mid = (first+last) // 2
		print("a[mid] = ", a[mid])
	if first > last:
		return 0
	else:
		return mid+1
r = bin(a,key)

if r == 0:
	print("Not found")
else:
	print("Place", r)
