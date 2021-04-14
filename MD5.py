import hashlib
from numba import jit

@jit(forceobj=True)
def md5(HASH, password):
	test_hash = hashlib.md5(password).hexdigest()
	if test_hash == HASH:
		print(HASH + ':' + password.decode())
		exit()