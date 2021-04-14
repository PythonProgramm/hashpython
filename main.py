#set up the logo and version
version = 1.3
logo = """
############################################################################
# _   _   _____   ____   _   _   __    _     _  _______    __   ___      _ #
#| | | | |  _  | |    | | | | | |  _\ \ \  / / |__   __| /   \  |   \   | |#
#| |_| | | |_| |  \ \   | |_| | ||_| | \ \/ /     | |   |  _  | | |\ \  | |#
#|  _  | |  _  |   \ \  |  _  | |  _/   \  /      | |   | |_| | | | \ \ | |#
#| | | | | | | | __/ /  | | | | | |     |  |      | |   |     | | |  \ \| |#
#|_| |_| |_| |_||___/   |_| |_| |_|     |__|      |_|    \___/  |_|   \___|#
#                                                                   v"""+str(version)+"""   #
#                                                                by HACK3R #
############################################################################"""

# Take imports of Threading, concurrent.future, argparse  and sys.argv
from argparse import ArgumentParser

# Take imports of the other module of this project.
from hashid import *
from MD4 import *
from MD5 import *
from SHA512WHIRLPOOL import *
from SHA224 import *
from SHA384 import *
from ntlm import *
from unix import *

# initial parser
parser = ArgumentParser()

# Set up arguments
parser.add_argument('-H', '--hash-file', nargs=1, required=True, help="hash file", dest='hashfile', type=str)
parser.add_argument('-m', '--method', nargs=1, default=[0], type=int, help='the method. 0 for dictinary, 1 for brute force', dest='method')
parser.add_argument('-r', '--range', nargs=2, dest='range', help='the the range for brute force')
parser.add_argument('-w', '--wordlist', nargs=1, dest='wordlist', help='The wordlist')
parser.add_argument('-t', '--type', nargs=1, dest='type', default=['auto'], help='type of hash')

args = parser.parse_args()
method = args.method[0]
hashes = set()
print(logo)
try:
	with open(args.hashfile[0]) as hashfile:
		found = 0
		for i in hashfile.readlines():
			hashes.add(i.strip("\n"))
			found += 1
	print("Loaded " + str(found) + " hashes")
	if found == 0:
		print("Loaded 0 hashes")
		exit(4)
except FileNotFoundError:
	print(args.hashfile[0] + ": No such file or directory")
	exit(3)

for Hash in hashes:
	if method == 0:
		if args.wordlist is None:
			print("USAGE:")
			print('-w/ --wordlist WORDLIST -H/ --hash HASH')
			exit(1)

		
		with open(args.wordlist[0], "rb") as w:
			pwds = set(w.read().splitlines())
		if args.type[0].upper() == 'AUTO':
			Type = getId(Hash)
			if 'md5'.upper() in Type:
				for i in Type:
					if i.lower() == 'md5':
						for pwd in pwds:
							md5(Hash, pwd)
						for pwd in pwds:
							nt(Hash, pwd)
						for pwd in pwds:
							lm(Hash, pwd)
					elif i.lower() == 'md4':
						for pwd in pwds:
							md4(Hash, pwd)
			elif 'sha512'.upper() in Type:
				for i in Type:
					if i.lower() == 'sha512':
						print("Try sha512")
						for pwd in pwds:
							sha512(Hash, pwd)
					elif i.lower() == 'whirlpool':
						print("Try whirlpool                                                        ")
						for pwd in pwds:
							whirlpool(Hash, pwd)
			elif 'sha224'.upper() in Type:
				for pwd in pwds:
					sha224(Hash, pwd)
			elif 'sha384'.upper() in Type:
				for pwd in pwds:
					sha384(Hash, pwd)
			elif "unix".upper() in Type:
				salt = getSalt(Hash)
				for pwd in pwds:
					UNIX(pwd, salt, Hash)
