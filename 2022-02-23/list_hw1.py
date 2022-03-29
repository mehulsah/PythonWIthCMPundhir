square = [1,4,9,16,25]
print (square)
print (square[0])
print (square[-1])
print (square[-3:])
print (square[:])
triangle = [2,3,4,34,23]
print (square + triangle)
cubes = [1,8,27,65,125]
cubes[3]=64
print(cubes)
cubes.append(216)
cubes.append(7**3)
print (cubes)
letters = ['a','b','c','d','e','f']
print (letters)
letters[2:4]=['C','D']
print (letters)
letters [2:4]=[]
print(letters)
print(len(letters))
x = [letters,cubes]
print(x)
print(x[0])
print(x[0][1])
a,b=0,1
while a<10:
	print(a)
	a,b=b,a+b