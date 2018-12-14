import zipfile
import re

with zipfile.ZipFile('channel.zip', 'r') as zipf:
	zipf.extractall('./channel')

nothing = '90052'
counter = 0
while True:
	counter += 1
	with open('./channel/' + nothing + '.txt') as f:
		text = f.readline()
		try:
			nothing = re.search('nothing is (\d+)', text).group(1)
		except AttributeError:
			print(counter, nothing, text)
			break

result = b''
with zipfile.ZipFile('channel.zip', 'r') as zipf:
	for info in zipf.infolist():
		result += info.comment

print(result.decode('utf-8'))
