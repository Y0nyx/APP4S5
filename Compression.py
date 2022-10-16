import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from zplane import zplane

def compression(img, percent):
    plt.imshow(img)
    covarianceImg = np.cov(img)
    valPropre, vecPropre = np.linalg.eig(covarianceImg)
    vecPropre = vecPropre.T
    produitDeMatrice = np.matmul(vecPropre, img)
    for i in range(int(len(produitDeMatrice)*(percent/100))):
        produitDeMatrice[len(produitDeMatrice)-1-i][:] = 0

    matplotlib.image.imsave("imgFinale\\compresse.png", arr=produitDeMatrice, cmap='gray')

    # passage_inv = np.inv(vecPropre)
    # imageFinale = np.matmul(vecPropre, img)
    imageFinale = np.matmul(np.linalg.inv(vecPropre), produitDeMatrice)
    matplotlib.image.imsave("imgFinale\\decompresse.png", arr=imageFinale, cmap='gray')


    #plt.imshow(produitDeMatrice)
    #plt.imshow(imageFinale)
    #plt.title(f"Image compressée de {percent}%")
    #plt.show()
