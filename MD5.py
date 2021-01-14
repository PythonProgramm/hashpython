import hashlib

def md5(HASH, password):
	test_hash = hashlib.md5(password.encode()).hexdigest()
	if test_hash == HASH:
		print(HASH + ':' + password)
		exit()