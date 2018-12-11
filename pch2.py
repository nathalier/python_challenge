__author__ = 'Nathalie'


def p2(file_name):
	with open(file_name) as f:
		text = f.read()
	from collections import Counter
	c = Counter(text)
	print(sorted(c.items(), key=lambda x: x[1]))


if __name__ == '__main__':
	print(p2('pch2.txt'))
