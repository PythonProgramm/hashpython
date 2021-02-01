import crypt

def getSalt(HASH):
    tmp = HASH.split("$")
    ctype = tmp[1]
    insalt = tmp[2]
    return "$" + ctype + "$" + insalt + "$"

def UNIX(pwd, salt, HASH):
    print("Try " + pwd, end="\r")
    test_hash = crypt.crypt(pwd, salt)
    if test_hash == HASH:
        print(HASH + ":" + pwd)
        exit(0)