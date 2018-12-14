import pickle

with open('GGy3qJ8W.p', 'rb') as f:
	data = pickle.load(f)
for item in data:
	print(''.join([c * n for c, n in item]))
