import os
import sys
import time
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
import operator
import math

img = nd.imread('images/digits.png')
nrow, ncol = img.shape[0:2]
xs = 10.
ys = xs*float(nrow)/float(ncol)

# plt.close(0)
# fig11, ax11 = plt.subplots(num=0,figsize=[xs,ys])
# fig11.subplots_adjust(0,0,1,1)
# ax11.axis('off')
# im11 = ax11.imshow(img)
# fig11.canvas.draw()

nums = img.reshape(50,20,100,20).transpose(0,2,1,3).reshape(5000,20,20)

fig12, ax12 = plt.subplots(num=1,figsize=[xs/1.5,xs/1.5])
fig12.subplots_adjust(0,0,1,1)
ax12.axis('off')
im12 = ax12.imshow(nums[0])
fig12.canvas.draw()

fig12.show()

nums_avg = np.array([nums[i*500:(i+1)*500].mean(0) for i in range(10)])

failureIndex = {}
fail = []
for ii in range(10):

    incorrect = 0
    errorDict = {}

    l = []

    for i in xrange(500):
        index = ii * 500 + i
        samp = nums[index]

        PT = nums_avg.reshape(10,400)
        P  = PT.transpose()
        PTPinv = np.linalg.inv(np.dot(PT,P))
        PTyy = np.dot(PT,samp.flatten())
        avec = np.dot(PTPinv,PTyy)
        l.append(avec)

        if np.argmax(avec) != ii:
            failureIndex[index] = np.argmax(avec)
            fail.append(index)
            incorrect += 1
            if np.argmax(avec) in errorDict:
                errorDict[np.argmax(avec)] += 1
            else:
                errorDict[np.argmax(avec)] = 1
        else:
            pass

    xs = 6
    ys = 8
    fig0, ax0 = plt.subplots(10,1,figsize=[xs,ys], sharex=True)

    sorted_x = sorted(errorDict.items(), key=operator.itemgetter(1), reverse = True)
    v = np.vstack(l)
    add = v.T


    for j in range(0,10):
        ax0[j].hist(add[j], bins = 100, color='cyan')
        [i.set_yticklabels('') for i in ax0]
        ax0[j].set_title("Known %s's Against %s's"% (ii,str(j)), fontsize=10)

    fig0.subplots_adjust(hspace=2)
    fig0.subplots_adjust(.1,.1,.95,.95)
    fig0.canvas.draw()

    fig0.show()

    print "%s%% of %s's were incorrectly identified, the most common guess for those failures was %s's" % \
    ((incorrect/500.0) * 100, ii, sorted_x[0][0])

t0 = time.time()
dt = 0.0
while dt<30.:
    i = int(math.floor(len(fail)*np.random.rand()))
    ii = fail[i]

    if dt == 0.0:
        im12.set_data(nums[ii])
        lab = ax12.text(0,0, 'Guess:  ', va = 'top', fontsize = 20, color = 'w')
        lab.set_text('Guess: {0}'.format(failureIndex[ii]))
    else:
        lab.remove()
        im12.set_data(nums[ii])
        lab = ax12.text(0,0, 'Guess:  ', va = 'top', fontsize = 20, color = 'w')
        lab.set_text('Guess: {0}'.format(failureIndex[ii]))

    fig12.canvas.draw()
    fig12.show()
    time.sleep(1.0)
    dt = time.time()-t0

plt.clf('all')

print "\n"
print "Removing zero point offset:\n"
failureIndex = {}
fail = []
for ii in range(10):

    incorrect = 0
    errorDict = {}

    l = []

    for i in xrange(500):
        index = ii * 500 + i
        samp = nums[index]

        PT1 = nums_avg.reshape(10,400)
        PT = np.vstack((PT1, np.ones(400)))
        P  = PT.transpose()
        PTPinv = np.linalg.inv(np.dot(PT,P))
        PTyy = np.dot(PT,samp.flatten())

        #Take only first 10 elements
        avec = np.dot(PTPinv,PTyy)
        avec = avec[0:10]
        l.append(avec[0:10])

        if np.argmax(avec) != ii:
            failureIndex[index] = np.argmax(avec)
            fail.append(index)
            #fail[index] = np.argmax(avec)
            incorrect += 1
            if np.argmax(avec) in errorDict:
                errorDict[np.argmax(avec)] += 1
            else:
                errorDict[np.argmax(avec)] = 1
        else:
            pass

    xs = 6
    ys = 8
    fig1, ax1 = plt.subplots(10,1,figsize=[xs,ys], sharex=True)

    sorted_x = sorted(errorDict.items(), key=operator.itemgetter(1), reverse = True)
    v = np.vstack(l)
    add = v.T

    for j in range(0,10):
        ax1[j].hist(add[j], bins = 100, color='cyan')
        [i.set_yticklabels('') for i in ax1]
        ax1[j].set_title("Known %s's Against %s's"% (ii,str(j)), fontsize=10)

    fig1.subplots_adjust(hspace=2)
    fig1.subplots_adjust(.1,.1,.95,.95)
    fig1.canvas.draw()

    print "%s%% of %s's were incorrectly identified, the most common guess for those failures was %s's" % \
    ((incorrect/500.0) * 100, ii, sorted_x[0][0])

plt.show()