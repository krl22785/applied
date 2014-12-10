import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf


img = mf(1.0*(255 - np.array([[e[2], e[1], e[0]] for e in nd.imread('images/ml.jpg').reshape(610560,3)[::2]]).\
            reshape(954,320,3)),[8,2,1]).clip(0,255).astype(np.uint8)


ysize = 10.
xsize = ysize*float(img.shape[1])/float(img.shape[0])

fig5, ax5 = plt.subplots(num=5,figsize=[xsize,ysize])
fig5.subplots_adjust(0,0,1,1)
fig5.canvas.set_window_title("modified mona lisa")
ax5.axis('off')
im5 = ax5.imshow(img)
fig5.canvas.draw()

plt.show()