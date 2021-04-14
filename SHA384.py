import hashlib
from numba import jit

@jit(forceobj=True)
def sha384(HASH, password):
	test_hash = hashlib.sha384(password).hexdigest()
	if test_hash == HASH:
		print(HASH + ':' + password)
		exit()