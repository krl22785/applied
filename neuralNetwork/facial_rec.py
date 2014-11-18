from pybrain.datasets.supervised import SupervisedDataSet 
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
import cv2

def loadImage(path):
	im = cv2.imread(path)
	return flatten(im)

def flatten(x):
	result = []
	for el in x:
		if hasattr(el, "__iter__") and not isinstance(el, basestring):
			result.extend(flatten(el))
		else:
			result.append(el)
	return result


if __name__ == "__main__":

	t = loadImage('other3copy.png')
	net = buildNetwork(len(t), .1*len(t), 1)
	ds = SupervisedDataSet(len(t), 1)

	ds = SupervisedDataSet(len(t), 1)

	ds.addSample(loadImage('other1copy.png'),(500,))
	ds.addSample(loadImage('ken1copy.png'),(1,))
	ds.addSample(loadImage('ken2copy.png'),(1,))
	ds.addSample(loadImage('other2copy.png'),(500,))
	ds.addSample(loadImage('ken3copy.png'),(1,))
	ds.addSample(loadImage('ken4copy.png'),(1,))
	ds.addSample(loadImage('ken5copy.png'),(1,))
	ds.addSample(loadImage('other3copy.png'),(500,))
	ds.addSample(loadImage('other4copy.png'),(500,))

	trainer = BackpropTrainer(net, ds)
	error = 10
	iteration = 0
	while error > 0.0001:
		error = trainer.train()
		iteration += 1
		print "Iteration: {0} Error {1}".format(iteration, error)

	print "\nResult: ", net.activate(loadImage('other4copy.png'))
	print "\nResult: ", net.activate(loadImage('ken6copy.png'))
	print "\nResult: ", net.activate(loadImage('ken7copy.png'))
	print "\nResult: ", net.activate(loadImage('other5copy.png'))
	print "\nResult: ", net.activate(loadImage('ken8copy.png'))

