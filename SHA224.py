import hashlib

def sha224(HASH, password):
	test_hash = hashlib.sha224(password.encode()).hexdigest()
	if test_hash == HASH:
		print(HASH + ':' + password)
		exit()