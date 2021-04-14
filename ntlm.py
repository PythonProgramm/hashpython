from passlib.hash import nthash, lmhash
from numba import jit

@jit(forceobj=True)
def nt(HASH, password):
    test_hash = nthash.hash(password)
    if test_hash == HASH:
        print(HASH + ':' + password)
        exit()

@jit(forceobj=True)
def lm(HASH, password):
    test_hash = lmhash.hash(password)
    if test_hash == HASH:
        print(HASH + ':' + password)
        exit()