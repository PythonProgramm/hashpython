import hashlib
from numba import jit

@jit(forceobj=True)

def whirlpool(HASH, password):
	test_hash = hashlib.new("whirlpool", password).hexdigest()
	if test_hash == HASH:
		print(HASH + ':' + password)
		exit()

@jit(forceobj=True)
def sha512(HASH, password):
	test_hash = hashlib.sha512(password.encode()).hexdigest()
	if test_hash == HASH:
		print(HASH + ':' +  password)
		exit()