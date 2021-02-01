import crypt
import hashlib
from passlib.hash import nthash, lmhash

print(hashlib.md5("kyosho12N".encode()).hexdigest())
print(nthash.hash("kyosho12N"))