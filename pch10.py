def v1():
	a = '1'
	res = ''
	for l in range(30):
		i, j = 0, 0
		while i < len(a):
			while j < len(a) and a[j] == a[i]:
				j += 1
			res += str(j - i) + a[i]
			i = j
		a, res = res, ''
	print(len(a))


def v2():
	import itertools
	a = '1'
	for i in range(30):
		a = "".join([str(len(list(f))) + d for d, f in itertools.groupby(a)])
	print(len(a))

def v3():
	import itertools
	import functools



v2()