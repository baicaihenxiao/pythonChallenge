from PIL import Image
import os, sys

print sys.argv[0:]

im = Image.open("dna.jpeg")
print im.format, im.size, im.mode
#im.show()
#print "%dx%d" % im.size, im.mode

print im.split()

'''
box = (100, 100, 400, 400)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)

im.show()
'''

im1 = Image.open("face.png")
print im1.format, im1.size, im1.mode
im1.show()
print im1.split()
r, g, b = im1.split()
print r, g, b
im1 = Image.merge("RGB", (b, g, r))
im1.show()







'''
pylab.imshow(im)
pylab.gray()
pylab.show()
'''
'''
plt.imshow(im)
plt.gray()
plt.show()
'''

'''
from PIL import Image
im = Image.open('face.png')

'''