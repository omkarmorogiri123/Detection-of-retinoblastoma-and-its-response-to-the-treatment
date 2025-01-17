# -*- coding: utf-8 -*-
"""imageprocessing1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oFmcoFqQw1XvQCC-IHWHpl7TFrE1lyLh
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

img1= plt.imread('C:/Users/PB/Desktop/imagep/imgs/4.1.04.tiff')

plt.imshow(img1)
plt.title('lady')
plt.show()

plt.imsave('C:/Users/PB/Desktop/imagep/output.png', img1)

img1= plt.imread('C:/Users/PB/Desktop/imagep/imgs/4.1.04.tiff')
print(img1)
print(img1.shape)

"""# Mask of image"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
img1= plt.imread('C:/Users/PB/Desktop/imagep/imgs/4.1.06.tiff')
nrows, ncols,channels = img1.shape
row, col =np.ogrid[:nrows, :ncols]
centre_row, centre_col = nrows/2, ncols/2
#print(row)
#print(col)
outer_mask= ((row- centre_row)**2 + (col-centre_col)**2 > (nrows/2)**2)
img1.setflags(write=1)
img1[outer_mask]=0
plt.imshow(img1)
plt.title('Masked image')
plt.show()

