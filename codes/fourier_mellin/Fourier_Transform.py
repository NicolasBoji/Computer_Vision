import cv2
import matplotlib.pyplot as plt
import numpy as np

def FT(img,radius,rep):
    '''Help:
    The function gives the fourier transform and the log-polar transform.
    img is the image which we will apply the transform.
    radius is the radius used during the log-polar transform.
    '''
    w, h = img.shape[::-1]
    center = ((w/2,h/2))  
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    dft_complex = dft_shift[:,:,0] + 1j*dft_shift[:,:,1]
    dft_abs = np.abs(dft_complex) +1

    magnitude_spectrum = 20*np.log(dft_abs)
    #Save and show the fourier transform
    plt.imshow(magnitude_spectrum,cmap='gray')
    plt.savefig(rep+'.jpg',cmap='gray')
    plt.show()
    magnitude_spectrum = cv2.logPolar(magnitude_spectrum,center,radius,cv2.INTER_LINEAR+cv2.WARP_FILL_OUTLIERS)
    return magnitude_spectrum
