import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import signal
import zplane
def revertAbberation(img, num, den):
    # La fonction es stable car les pôles sont dans le cercle unitaire
    #zplane.zplane(den, num)

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

def ComparaisonFiltre(wp, ws, gpass, gstop, fs):
    N = np.zeros(4)
    Wn = np.zeros(4)
    types = ("Butterworth", "Chebyshev 1", "Chebyshev 2", "elliptique")
    N[0], Wn[0] = signal.buttord(wp, ws, gpass, gstop, analog=False, fs=fs)
    N[1], Wn[1] = signal.cheb1ord(wp, ws, gpass, gstop, analog=False, fs=fs)
    N[2], Wn[2] = signal.cheb2ord(wp, ws, gpass, gstop, analog=False, fs=fs)
    N[3], Wn[3] = signal.ellipord(wp, ws, gpass, gstop, analog=False, fs=fs)
    Nmin = np.min(N)
    Nargmin = np.argmin(N)
    print(types[Nargmin], "with an order of ", Nmin, "is the minimal order Filter")