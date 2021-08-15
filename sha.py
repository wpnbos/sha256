def binary(string):
	"""
	returns binary representation of input string	
	"""
	return ' '.join(format(ord(c), "08b") for c in string)

def blen(binstring):
	"""
	returns length of binary string (ignoring whitespaces)
	"""
	c = 0
	for i in binstring: 
		if i != " ":
			c += 1
	return c

def pad(binstring):
	"""
	returns padded binary string 
	"""
	padsize = (int(blen(binstring) / 512) + 1) * 512 - 64
	binstring = binstring + "0000000"
	padsize = padsize - blen(binstring)
	padding = " 00000000" * int(padsize / 8)
	binstring += padding
	return binstring
	

def sha256(string):
	hashed = binary(string) + " 1"
	hashed = pad(hashed)
	hashed += " " + format(blen(binary(string)), "08b")
	return hashed

print(sha256("hello world"))