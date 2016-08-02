from scipy import misc
import matplotlib.pyplot as plt
'''f = misc.face()
misc.imsave('face.png', f) # uses the Image module (PIL)
plt.imshow(f)
plt.show()'''
face = misc.imread('face.png')
print type(face)
print face.shape, face.dtype
face.tofile('face.raw')
face_from_raw = np.fromfile('face.raw', dtype=np.uint8)
'''
from PIL import Image
im = Image.open('face.png')
plt.imshow(im)
plt.show()
'''