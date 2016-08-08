#2016-8-6 19:02:07
#level 7: http://www.pythonchallenge.com/pc/def/oxygen.html


from PIL import Image
import sys


im = Image.open("oxygen.png")
#pixels = list(im.getdata())
#print pixels
print im.format, im.size, im.mode
'''
r = 0
g = 0
b = 0
a = 0
for i in range(0, 629):
	r1, g1, b1 , a1= im.getpixel((i,47))
	#print i, im.getpixel((i,47)), chr(r)
	#print
	if (r1 != r):
		r = r1
		sys.stdout.write(chr(r))
'''	
for i in range(0, 629, 7):
	r, g, b , a= im.getpixel((i,47))
	sys.stdout.write(chr(r))

print 
print chr(105)
print chr(110)
print chr(116)
print chr(101)
print chr(103)
print chr(114)
print chr(105)
print chr(116)
print chr(121)

#1. download the oxygen.png, there are a strip of gray lattices in the middle, open the photo with windows Paint.
#2. you can see that the x coodination of those gray lattices range from 0 to 629, the width of each lattice is 7 pixels, the height is 47(46£¬48 is only OK)
#the answer is to get the RGB value of each lattices, because the lattices is gray level, so R=G=B. convert the R(or G, B) value to char and print them.
#3. output: smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]pe_
#4. convert [105, 110, 116, 101, 103, 114, 105, 116, 121] to char again and you will get the answer "integrity"
	
#the next level website: http://www.pythonchallenge.com/pc/def/integrity.html
