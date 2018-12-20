from PIL import Image

im = Image.open('oxygen.png')
print(im.format, im.size, im.mode)

for y in range(im.height):
	pix = im.getpixel((0, y))
	done = False
	if pix[0] == pix[1] and pix[0] == pix[2]:
		eq, x = True, 0
		while eq:
			print(f'{chr(pix[0])}', end='')
			x += 7
			pix = im.getpixel((x, y))
			eq = (pix[0] == pix[1] and pix[0] == pix[2])
		done = True
	if done:
		print()
		break

for x in [105, 110, 116, 101, 103, 114, 105, 116, 121]:
	print(chr(x), end='')
