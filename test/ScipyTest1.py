from PIL import Image
import matplotlib.pyplot as plt
import pylab

'''
im = misc.imread('face.png')
print type(im)
print im.shape, im.dtype
print im.max(), im.min()
'''
#dna = Image.open('dna.jpeg')
dna = misc.imread('dna.jpeg')
print type(dna)
print dna.shape, dna.dtype
print dna.max(), dna.min()


T = misc.thresholding.otsu(dna)
pylab.imshow(dna > T)
pylab.show()




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