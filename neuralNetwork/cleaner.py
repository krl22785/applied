import os
import glob
from PIL import Image
from sys import argv

def changeType(img):
	im = Image.open(img)
	first = img.split(".")[0]
	im.save(first+".png")

def resizespec(img,height,width):
	im = Image.open(img).convert('LA')
	w,h = im.size
	newIm = im.resize((height,width))
	first = img.split(".")[0]
	newIm.save(first+"copy.png")

def jpegToPng():
	images = glob.glob("*.jpeg")
	for image in images:
		changeType(image)
	images = glob.glob("*.jpg")
	for image in images:
		changeType(image)

def resize(height,width):
	images = glob.glob("*.png")
	for image in images:
		resize(image,height,width)

for i in xrange(8,11):
	jpegToPng()
	img="cat"+str(i)+'.png'
	resizespec(img,40,40)
	#img='dog'+str(i)+'.png'
	#resizespec(img,40,40)

	#img='gorilla'+str(i)+'.png'
	#resizespec(img,40,40)

	#img='giraffe'+str(i)+'.png'
	#resizespec(img,40,40)

	#img='alligator'+str(i)+'.png'
	#resizespec(img,40,40)