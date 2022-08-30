import cv2
import matplotlib.pyplot as plt
import numpy as np


def cross_correlation(main,method,sample, rep):
    '''Help:
    The function aims to give the cross-correlation between a main picture and a sample.
    main is the main picture used in cross-correlation. It's also the one which we will apply the mosaic.
    method is the method used during the picture matching. ( a string is required)
    sample is the second picture used in the matching.
    '''
    own1=np.concatenate((main, main), axis=0)
    own2=np.concatenate((main, main), axis=0)
    main=np.concatenate((own1, own2), axis=1)
    w, h = sample.shape[::-1]
    # Apply template Matching
    method=eval(method)
    res = cv2.matchTemplate(main,sample,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(main,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(main,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(method)
    plt.savefig(rep+'.jpg',cmap='gray')
    plt.show()
