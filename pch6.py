import zipfile
import re

with zipfile.ZipFile('channel.zip', 'r') as zipf:
	nothing = '90052'
	comments = b''
	while True:
		filename = nothing + '.txt'
		comments += zipf.getinfo(filename).comment
		text = zipf.read(filename)
		try:
			nothing = re.search(b'nothing is (\d+)', text).group(1).decode('utf-8')
		except AttributeError:
			print(text)
			break

print(comments.decode('utf-8'))
