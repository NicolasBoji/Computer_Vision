import cv2
import matplotlib.pyplot as plt
import numpy as np

def mean(img):
    '''Help:
    The goal of this function is to return the mean value of the image.
    img is the picure needed to calculate the mean.
    '''
    M=0
    w, h = img.shape[::-1]
    for i in range(w):
        for j in range(h):
            M+=img[i][j]
    return (M/(w*h))

def correlation_coefficient(magnitude_spectrum,magnitude_spectrum2):
    '''Help:
    The function returns the correlation coefficient between two picures.
    magnitude_spectrum  is the first picture used in the matching.
    magnitude_spectrum2 is the second picture to calculate the coefficient. 
    '''
    C1=0
    C2=0
    C3=0
    M1= mean(magnitude_spectrum)
    M2= mean(magnitude_spectrum2)
    w, h = magnitude_spectrum.shape[::-1]
    for i in range(w):
        for j in range(h):
            C1 += (magnitude_spectrum[i][j] - M1) * (magnitude_spectrum2[i][j] - M2)
            C2 += (magnitude_spectrum[i][j] - M1)**2
            C3 += (magnitude_spectrum2[i][j] - M2)**2
    C4=np.sqrt(C2*C3)
    Cm= C1/C4
    return  Cm
