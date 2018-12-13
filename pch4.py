__author__ = 'Nathalie'

import urllib.request
import re


url_base = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '12345'
counter = 0
answer_re = re.compile(b'next nothing is (\d*)')
while True:
	url = url_base + nothing
	counter += 1
	with urllib.request.urlopen(url) as response:
		html = response.read()
	next_phrase = answer_re.search(html)
	if next_phrase:
		nothing = next_phrase.group(1).decode('utf-8')
	elif html.decode('utf-8').find('Divide by two', ) >= 0:
		nothing = str(int(nothing) / 2)
	else:
		break
print(counter, html)
