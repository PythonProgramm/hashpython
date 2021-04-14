import crypt

def getSalt(HASH):
    tmp = HASH.split("$")
    ctype = tmp[1]
    insalt = tmp[2]
    return "$" + ctype + "$" + insalt + "$"

from numba import jit

@jit(forceobj=True)
def UNIX(pwd, salt, HASH):
    test_hash = crypt.crypt(pwd, salt)
    if test_hash == HASH:
        print(HASH + ":" + pwd)
        exit(0)