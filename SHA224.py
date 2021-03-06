import hashlib
from numba import jit

@jit(forceobj=True)
def sha224(HASH, password):
	test_hash = hashlib.sha224(password).hexdigest()
	if test_hash == HASH:
		print(HASH + ':' + password.decode())
		exit()