import hashlib

def sha384(HASH, password):
	test_hash = hashlib.sha384(password.encode()).hexdigest()
	if test_hash == HASH:
		print(HASH + ':' + password)
		exit()