#2016-8-1 15:26:14
#level 5: http://www.pythonchallenge.com/pc/def/peak.html

import urllib, re
import matplotlib.pyplot as plt
from PIL import Image
from scipy import misc


#handle = urllib.urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")
#misc.imsave('oxygen.png', Image.open(handle)) 


#Image.open('oxygen.png')
#plt.imshow()
#plt.show()


i = Image.open("oxygen.png") # http://www.pythonchallenge.com/pc/def/oxygen.png
row = [i.getpixel((x, 45)) for x in range(0, i.size[0], 7)]
ords = [r for r, g, b, a in row if r == g == b]

print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords))))))


'''
another method:	
for iter in file:
	print ''.join(elmt[0] * elmt[1] for elmt in iter)
'''
		
#the next level website: http://www.pythonchallenge.com/pc/def/channel.html
