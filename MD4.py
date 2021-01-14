from hashlib import new


def md4(HASH, password):
	test_hash = new('md4', password.encode()).hexdigest()
	if test_hash ==  HASH:
		print(HASH + ':' + password)
		exit()