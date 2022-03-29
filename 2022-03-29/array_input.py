abc = input("Enter a string: ")
print(abc)
arr = abc.split(" ")
print(arr)
t3 = list(map(int, arr))
print(t3)

# use for loop to cast to int
res = [int(x) for x in arr]
print(res)


res = []
for x in arr:
	res.append(int(x))
print(res)