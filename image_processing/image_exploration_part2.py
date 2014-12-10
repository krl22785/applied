import os
import sys
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import numpy as np

dpath = sys.argv[1]
fname = sys.argv[2]
infile = os.path.join(dpath,fname)
img = nd.imread(infile)

## Plot Mona Lisa
nrow = img.shape[0]
ncol = img.shape[1]
xs = 6.5
ys = xs * float(nrow)/float(ncol)

fig0, ax0 = plt.subplots(num=0,figsize=[xs,ys])
ax0.axis('off')
fig0.subplots_adjust(0,0,1,1)
fig0.canvas.set_window_title(fname)
img0 = ax0.imshow(img)
fig0.canvas.draw()
fig0.show()

## Plot Historgram
fig1, ax1 = plt.subplots(3,1,num=1,figsize=[2*xs,xs])
col = ['r','g','b']

for i in range(0,3):
    ax1[i].hist(img[:,:,i].flatten(),bins=256,range=[0,255], normed=True, color = col[i])

[i.set_yticklabels('') for i in ax1]

fig1.subplots_adjust(hspace=.5)
ax1[0].set_title('Red')
ax1[1].set_title('Green')
ax1[2].set_title('Blue')
fig1.canvas.draw()
fig1.show()

## INFINITE LOOP

count = 0
while True:
    pts = fig1.ginput(3)
    x1 = int(round(pts[0][0]))
    x2 = int(round(pts[1][0]))
    x3 = int(round(pts[2][0]))

    if count == 0:

        rng1 = ax1[0].axvspan(x1+5, x1-5, facecolor = 'orange', alpha = .2)
        rng2 = ax1[1].axvspan(x2+5, x2-5, facecolor = 'orange', alpha = .2)
        rng3 = ax1[2].axvspan(x3+5, x3-5, facecolor = 'orange', alpha = .2)

    else:

        spn1 = rng1.get_xy()
        spn1[:,0] = [x1-5,x1-5,x1+5,x1+5,x1-5]
        rng1.set_xy(spn1)

        spn2 = rng1.get_xy()
        spn2[:,0] = [x2-5,x2-5,x2+5,x2+5,x2-5]
        rng2.set_xy(spn2)

        spn3 = rng3.get_xy()
        spn3[:,0] = [x3-5,x3-5,x3+5,x3+5,x3-5]
        rng3.set_xy(spn3)

    fig1.canvas.draw()

    count += 1

    img2 = img.copy()
    cc = [x1, x2, x3]

    for i in range(3):
        img2[:,:,i][(img2[:,:,i] > (cc[i] + 5)) | (img2[:,:,i] < (cc[i] - 5))] = img2[:,:,i][(img2[:,:,i] > (cc[i] + 5)) | (img2[:,:,i] < (cc[i] - 5))] * .25

    img0.set_data(img2.clip(0,255).astype(np.uint8))
    fig0.canvas.draw()

    fig0.show()


