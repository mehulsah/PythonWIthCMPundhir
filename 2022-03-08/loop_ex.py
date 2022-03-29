

#For type-2 statement
users={'Hans':'Active','Mehul':'Inactive','Saurabh':'Active'}
for user,status in users.copy().items():
	if status == 'inactive':
		del users[user]
print(users)

active_users = {}
for user, status in users.items():
	if status == 'active':
		active_users[user] = status
