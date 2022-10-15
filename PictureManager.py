import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import signal
import zplane
def revertAbberation(img, num, den):
    # La fonction es stable car les pôles sont dans le cercle unitaire
    zplane.zplane(den, num)

    # Pour comparer, enregistrer l'image avec l'abberation
    mpimg.imsave("img\\goldhill_abberations.png", arr=img)

    # Filtre et enregistre l'image finale
    FiltedImg = signal.lfilter(den, num, img)
    mpimg.imsave("imgFinale\\goldhill_abberations_Finale.png", arr=FiltedImg)

def rotation90degree (img):
    # Trouver les longueur des column and row
    row = len(img)
    column = len(img[0])
    EmptyArray = np.zeros((column, row))
    # Effectuer le changement de coordonne grace a une double for loop
    for i in range(0, row):
        for j in range(0, column):
            coordX = -row + 1 + i
            coordY = column - 1 - j
            # Multiplie
            x, y = np.matmul([[0, 1], [-1, 0]], [coordX, coordY])
            EmptyArray[x][y] = img[coordX][coordY]
    mpimg.imsave("imgFinale\\goldhill_rotate_Finale.png", arr=EmptyArray)


