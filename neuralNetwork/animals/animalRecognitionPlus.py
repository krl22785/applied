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
 
    t = loadImage('dog1copy.png')
    
    net = buildNetwork(len(t), .03*len(t), 1)
    ds = SupervisedDataSet(len(t), 1)
    
    ds.addSample(loadImage('dog1copy.png'),(0,))
    ds.addSample(loadImage('dog2copy.png'),(0,))
    ds.addSample(loadImage('dog3copy.png'),(0,))
    ds.addSample(loadImage('dog4copy.png'),(0,))
    ds.addSample(loadImage('dog5copy.png'),(0,))
    ds.addSample(loadImage('dog6copy.png'),(0,))
    ds.addSample(loadImage('dog7copy.png'),(0,))
    ds.addSample(loadImage('giraffe1copy.png'),(1,))
    ds.addSample(loadImage('giraffe2copy.png'),(1,))
    ds.addSample(loadImage('giraffe3copy.png'),(1,))
    ds.addSample(loadImage('giraffe4copy.png'),(1,))
    ds.addSample(loadImage('giraffe5copy.png'),(1,))
    ds.addSample(loadImage('giraffe6copy.png'),(1,))
    ds.addSample(loadImage('giraffe7copy.png'),(1,))
    ds.addSample(loadImage('alligator1copy.png'),(2,))
    ds.addSample(loadImage('alligator2copy.png'),(2,))
    ds.addSample(loadImage('alligator3copy.png'),(2,))
    ds.addSample(loadImage('alligator4copy.png'),(2,))
    ds.addSample(loadImage('alligator5copy.png'),(2,))
    ds.addSample(loadImage('alligator6copy.png'),(2,))
    ds.addSample(loadImage('alligator7copy.png'),(2,))
    ds.addSample(loadImage('alligator8copy.png'),(2,))
    ds.addSample(loadImage('gorilla1copy.png'),(3,))
    ds.addSample(loadImage('gorilla2copy.png'),(3,))
    ds.addSample(loadImage('gorilla3copy.png'),(3,))
    ds.addSample(loadImage('gorilla4copy.png'),(3,))
    ds.addSample(loadImage('gorilla5copy.png'),(3,))
    ds.addSample(loadImage('gorilla6copy.png'),(3,))
    ds.addSample(loadImage('gorilla7copy.png'),(3,))
    ds.addSample(loadImage('cat1copy.png'),(4,))
    ds.addSample(loadImage('cat2copy.png'),(4,))
    ds.addSample(loadImage('cat3copy.png'),(4,))
    ds.addSample(loadImage('cat4copy.png'),(4,))
    ds.addSample(loadImage('cat5copy.png'),(4,))
    ds.addSample(loadImage('cat6copy.png'),(4,))
    ds.addSample(loadImage('cat7copy.png'),(4,))
    ds.addSample(loadImage('cat8copy.png'),(4,))

    trainer = BackpropTrainer(net, ds)
    error = 10
    iteration = 0
    while error > 0.0001:
        error = trainer.train()
        iteration += 1
        print "Iteration: {0} Error {1}".format(iteration, error)
    
    ### pick an animal image
    
    image1 = 'gorilla7copy.png'    
    
    output = net.activate(loadImage(image1))
    
    if round(output) == 0:
        print "\nPicture {0} has a dog.".format(image1)
    elif round(output) == 1:
        print "\nPicture {0} has a giraffe.".format(image1)
    elif round(output) == 2:
        print "\nPicture {0} has a alligator.".format(image1)
    elif round(output) == 3:
        print "\nPicture {0} has a gorilla.".format(image1)
    elif round(output) == 4:
        print "\nPicture {0} has a cat.".format(image1)
    else:
        print "\nPicture {0} has an unrecognizable animal.".format(image1)