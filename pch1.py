__author__ = 'Nathalie'


def p1_mine(s):
	import string
	source = string.ascii_lowercase
	outcome = {}
	for c in source[:-2:]:
		outcome[c] = chr(ord(c) + 2)
	outcome[source[-2]] = source[0]
	outcome[source[-1]] = source[1]

	result = ''
	for c in s:
		if c in outcome:
			result += outcome[c]
		else:
			result += c
	return result


def p1_recom(s):
	import string

	source = string.ascii_lowercase
	outcome = ''
	for c in source[:-2:]:
		outcome += chr(ord(c) + 2)
	outcome += source[:2]

	tt = str.maketrans(source, outcome)
	result = str.translate(s, tt)
	return result


if __name__ == '__main__':
	print(p1_recom("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."))
