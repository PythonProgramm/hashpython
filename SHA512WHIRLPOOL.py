import hashlib


def whirlpool(HASH, password):
	test_hash = hashlib.new("whirlpool", password.encode()).hexdigest()
	if test_hash == HASH:
		print(HASH + ':' + password)
		exit()

def sha512(HASH, password):
	test_hash = hashlib.sha512(password.encode()).hexdigest()
	if test_hash == HASH:
		print(HASH + ':' +  password)
		exit()