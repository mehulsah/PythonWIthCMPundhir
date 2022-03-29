# Data Type 
# 1. Number
# 2. String
# 3. List, tuple, range
# 4. Tuple
# 5. Set, frozenset
# 6. Dict
# 7. Bool
# 8. Bytes

# defining different type of variables
a = 12
name = "Mehul"
hobbies = ("Play Footbal", "Coding")
friends = ["Agam", "Mohit", "Karan"]
messiTrophies = {"2009: UCL", "2011 Laliga", "2009: UCL"}
family = {"Mother": "Mrs. Vandana", "Father": "Mr. Deepak", "Pet": "Tomy"}
isGirlfriend = True
scores = range(0, 10)

print("----------*********---------")
# printing type of variable using type() function
print(type(a), a)
print(type(name), name)
print(type(hobbies), hobbies)
print(type(messiTrophies), messiTrophies)
print(type(friends), friends)
print(type(family), family)
print(type(isGirlfriend), isGirlfriend)
print(type(scores), scores)

print("----------*********---------")
# printing collection types
print(name[2:4])
print(hobbies[1])
print(friends[1:3])
print(family["Mother"])

# printing boolean
print(isGirlfriend)

# using 'in' operator with set to check whether it contains item or not
print("2009: UCL" in messiTrophies)

print("----------*********---------")
# printing all items in the set using for loop
for x in messiTrophies:
	print(x)
print("----------*********---------")
# example of using 'in' to check for values in range
print(2 in scores)
print("----------*********---------")
# printing all values in range 'scores'
for x in scores:
	print(x, end=" ")
print("\n----------*********---------")
print(family.items())
# iterating over a copy of family dict to change Pet name
for key, value in family.copy().items():
	if key=="Pet":
		family["Pet"] = "Scooby"
print(family["Pet"])
print("----------*********---------")
# adding a family member
family["Brother"] = ["Saurav", "Gaurav","Manav","Samarth"]
print(family)
print("----------*********---------")
#selecting brother with names starting with S from dict 'family'
brother_S = []
for bro in family["Brother"]:
	if bro[0] == "S":
		brother_S.append(bro)
for x in brother_S:
	print(x)
print("----------*********---------")