#import scipy
#scipy.misc
import scipy.misc

f = scipy.misc.face()
scipy.misc.imsave('face.png', f)

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()