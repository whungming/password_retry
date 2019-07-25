password = 'a123456'
i = 3 # the chance left

while i > 0:
	i = i - 1
	pwd = input('enter pasword: ')
	if pwd == password:
		print('sign in success!')
		break
	else:
	    print('wrong password!')
	    if i > 0:
		    print('only has', i, 'chance left')
	    else:
		    print('no more chance to sign in')