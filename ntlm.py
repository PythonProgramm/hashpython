from passlib.hash import nthash, lmhash

def nt(HASH, password):
    test_hash = nthash.hash(password)
    if test_hash == HASH:
        print(HASH + ':' + password)
        exit()

def lm(HASH, password):
    test_hash = lmhash.hash(password)
    if test_hash == HASH:
        print(HASH + ':' + password)
        exit()