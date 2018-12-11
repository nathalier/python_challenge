__author__ = 'Nathalie'


def p3(file_name):
	with open(file_name) as f:
		text = f.read()
	import re
	return ''.join(re.findall("[^A-Z][A-Z]{3}([a-z]){1}[A-Z]{3}[^A-Z]", text))


if __name__ == '__main__':
	print(p3('pch3.txt'))
