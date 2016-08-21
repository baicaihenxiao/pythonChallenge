#2016-8-21 14:07:00
#level 11: http://www.pythonchallenge.com/pc/return/5808.html

#username:huge password:file

encode = 'utf-8'


from PIL import Image, ImageDraw
import urllib

'''
#fetch file from web
webJpg = urllib.urlopen('http://www.pythonchallenge.com/pc/return/cave.jpg')

cave = Image.open(webJpg)

cave.save('cave.jpg')

'''

cave = Image.open('cave.jpg')

print cave.format, cave.size, cave.mode

width, height = cave.size

'''
for i in range(20):
	for j in range(20):
			print cave.getpixel((i, j))

'''

for i in range(height):
	for j in range(width):
		if ((i + j) % 2 == 1):
			cave.putpixel((j, i), (0, 0, 0))

cave.show()
#cave.save(r'C:\Users\baica\Desktop\cave.jpg')


#1. the title of the page is 'odd even'
#2. print the pixel, you can find the pattern;
#3. remove the odd pixels and show the new photo;
#4. there's a dim string 'evil' on the up-right of the photo

#the next level website: http://www.pythonchallenge.com/pc/return/evil.html
