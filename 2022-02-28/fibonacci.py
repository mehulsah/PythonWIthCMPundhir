def fib1():
	a = 0
	b = 1
	print(a,",",b, end=", ")
	for i in range(10):
		c = a + b
		print(c, end=", ")
		a = b
		b = c

fib1()

print()

def fib2(n):
	a, b = 0, 1
	for i in range(n):
		print(a, end=", ")
		a, b = b, a+b

fib2(10)

def fib3():
	a,b=0,1
	for i in range(n):
		print(a,end=", ")
		a, b = b, a+b