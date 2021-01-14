#set up the logo and version
version = 1.0
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
import concurrent.futures
import threading
from argparse import ArgumentParser
from sys import argv

# Take imports of the other module of this project.
from hashid import *
from MD4 import *
from MD5 import *
from SHA512WHIRLPOOL import *
from SHA224 import *
from SHA384 import *

# initial parser
parser = ArgumentParser()

# Set up arguments
parser.add_argument('-H', '--hash', nargs=1, required=True, help="hash", dest='hash')
parser.add_argument('-m', '--method', nargs=1, default=[0], type=int, help='the method. 0 for dictinary, 1 for brute force', dest='method')
parser.add_argument('-r', '--range', nargs=2, dest='range', help='the the range for brute force')
parser.add_argument('-w', '--wordlist', nargs=1, dest='wordlist', help='The wordlist')
parser.add_argument('-t', '--type', nargs=1, dest='type', default=['auto'], help='type of hash')

args =  parser.parse_args()

method = args.method[0]
Hash = args.hash[0]

if method == 0:
	if args.wordlist is None:
		print("USAGE:")
		print('-w/ --wordlist WORDLIST -H/ --hash HASH')
		exit(1)
	print(logo)
	pwds = set()
	with open(args.wordlist[0]) as w:
		for j in w:
			pwds.add(j.strip("\n"))
	if args.type[0].upper() == 'AUTO':
		print("Try to find type of hash")
		Type = getId(Hash)
		if 'md5'.upper() in Type:
			print("Hash found. It's md5 or md4.")
			for i in Type:
				if i.lower() == 'md5':
					print("Try md5")
					for pwd in pwds:
						t = threading.Thread(target=md5, args=(Hash, pwd))
						t.start()
						print("Try " + pwd, end="\r")
				elif i.lower() == 'md4':
					print("Try md4                                                        ")

					for pwd in pwds:
						t = threading.Thread(target=md4,  args=(Hash, pwd))
						t.start()
						print("Try " + pwd, end="\r")
		elif 'sha512'.upper() in Type:
			print("Hash found. It's sha512 or whirlpool.")
			for i in Type:
				if i.lower() == 'sha512':
					print("Try sha512")
					for pwd in pwds:
						t = threading.Thread(target=sha512, args=(Hash, pwd))
						t.start()
						print("Try " + pwd, end="\r")
				elif i.lower() == 'whirlpool':
					print("Try whirlpool                                                        ")

					for pwd in pwds:
						t = threading.Thread(target=whirlpool,  args=(Hash, pwd))
						t.start()
						print("Try " + pwd, end="\r")
		elif 'sha224'.upper() in Type:
			print("Hash found. It's sha224")
			print("Try sha224")


			for pwd in pwds:
				t = threading.Thread(target=sha224, args=(Hash, pwd))
				t.start()
				print("Try " + pwd, end="\r")
		elif 'sha384'.upper() in Type:
			print("Hash found. It's sha348")


			for pwd in pwds:
				t = threading.Thread(target=sha384, args=(Hash, pwd))
				t.start()
				print("Try " + pwd, end="\r")


print('                                                                         ', end='')
