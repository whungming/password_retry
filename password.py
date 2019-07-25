password = 'a123456'
i = 3 # the chance left
while True:
	pwd = input('enter pasword: ')
	if pwd == password:
		print('sign in success!')
		break
	else:
		i = i - 1
		print('wrong password! only has', i, 'chance left')
		if i == 0:
			break