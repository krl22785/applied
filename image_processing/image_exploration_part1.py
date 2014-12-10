import os
import sys
import scipy.ndimage as nd
import matplotlib.pyplot as plt

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

## Plot Histograms for Colors

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


# click on top left and bottom right to get new red, green, blue color distribution via histogram
while True:

    pts = fig0.ginput(2)
    x1, y1 = pts[0]
    x2, y2 = pts[1]

    x1 = int(round(x1))
    x2 = int(round(x2))
    y1 = int(round(y1))
    y2 = int(round(y2))

    col = ['r','g','b']

    if x1 == x2 and y1 == y2:
        print pts

        [ax1[i].cla() for i in range(3)]

        for i in range(0,3):
            ax1[i].hist(img[:,:,i].flatten(),bins=256,range=[0,255], normed=True, color = col[i])

        [i.set_yticklabels('') for i in ax1]

        fig1.subplots_adjust(hspace=.5)
        ax1[0].set_title('Red')
        ax1[1].set_title('Green')
        ax1[2].set_title('Blue')
        fig1.canvas.draw()


    elif x1 <= x2 and y1 <= y2:
        print pts
        img2 = img[x1:x2,y1:y2,:]

        [ax1[i].cla() for i in range(3)]

        col = ['r','g','b']

        for i in range(0,3):
            ax1[i].hist(img2[:,:,i].flatten(),bins=256,range=[0,255], normed=True, color = col[i])

        [i.set_yticklabels('') for i in ax1]

        ax1[0].set_title('Red')
        ax1[1].set_title('Green')
        ax1[2].set_title('Blue')
        fig1.subplots_adjust(hspace=.7)
        fig1.canvas.draw()

    else:
        break

    fig1.show()

