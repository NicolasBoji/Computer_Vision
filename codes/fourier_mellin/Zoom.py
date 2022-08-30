import cv2
import matplotlib.pyplot as plt
import numpy as np

def zoom(cv2Object, scale):
    ''' Help:
    The goal of this function is to zoom our picture while keeping the original size.
    The first argument is the image we want to zoom.
    The second argument is the zoom we decide to use
    nota bene : a zoomsize equals to 1.49 means we are zooming by 2%, another one set at 1.20 means 60% etc...
    '''
    cv2object=cv2Object
    height, width = cv2object.shape

    #prepare the crop
    centerX,centerY=int(height/2),int(width/2)
    radiusX,radiusY= int(scale*height),int(scale*width)

    minX,maxX=centerX-radiusX,centerX+radiusX
    minY,maxY=centerY-radiusY,centerY+radiusY

    cropped = cv2object[minX:maxX, minY:maxY]
    resized_cropped = cv2.resize(cropped, (width, height))
    return resized_cropped
