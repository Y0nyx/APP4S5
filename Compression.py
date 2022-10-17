import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from zplane import zplane

def compression(img, percent):
    covariance= np.cov(img)
    valPropre, vecPropre = np.linalg.eig(covariance)
    vecPropre = np.transpose(vecPropre)
    matriceDePassage = np.matmul(vecPropre, img)
    for i in range(int(len(matriceDePassage)*(percent/100))):
        matriceDePassage[len(matriceDePassage)-1-i][:] = 0

    matplotlib.image.imsave("imgFinale\\compresse.png", arr=matriceDePassage, cmap='gray')


    #Decompressé l'image
    imageDecompresse = np.matmul(np.linalg.inv(vecPropre), matriceDePassage)
    matplotlib.image.imsave("imgFinale\\ "+ str(percent) + "decompresse.png", arr=imageDecompresse, cmap='gray')

    plt.subplot(1, 2, 1)
    plt.imshow(matriceDePassage, cmap ='gray')
    plt.title(f"Image compressée de {percent}%")
    plt.subplot(1, 2, 2)
    plt.imshow(imageDecompresse, cmap ='gray')
    plt.title(f"Image décompressé suivant la compresse de {percent}%")
    plt.show()
