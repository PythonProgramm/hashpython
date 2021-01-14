def getId(HASH):
	if len(HASH) == 32:
		return ('MD5', 'MD4')
	elif len(HASH) == 128:
		return ("SHA512", "WHIRLPOOL")
	elif len(HASH) == 64:
		return ("SHA256")
	elif len(HASH) == 96:
		return ("SHA384")
	elif len(HASH) == 40:
		return ("SHA1")
	elif len(HASH) == 56:
		return ("SHA224")
