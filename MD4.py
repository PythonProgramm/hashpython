from hashlib import new
from numba import jit

@jit(forceobj=True)
def md4(HASH, password):
	test_hash = new('md4', password).hexdigest()
	if test_hash ==  HASH:
		print(HASH + ':' + password)
		exit()