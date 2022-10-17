import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import signal
import zplane
def revertAbberation(img, num, den):
    # Filtre et enregistre l'image finale
    FiltedImg = signal.lfilter(den, num, img)

    plt.subplot(1, 2, 1)
    plt.imshow(img , cmap="gray")
    plt.title("Image avec aberrations")
    plt.subplot(1, 2, 2)
    plt.imshow(FiltedImg, cmap="gray")
    plt.title("Image sans abbberations")
    plt.show()

    return(FiltedImg)

def rotation90degree(img):
    # Trouver les longueur des column and row
    row = len(img)
    column = len(img[0])
    EmptyArray = np.zeros((column, row))
    # Effectuer le changement de coordonne grace a une double for loop
    for i in range(0, row):
        for j in range(0, column):
            coordX = -row + 1 + i
            coordY = column - 1 - j
            # Multiplie les matrice ensemble pour obtenir les nouvelles valeurs de x et y
            x, y = np.matmul([[0, 1], [-1, 0]], [coordX, coordY])
            EmptyArray[x][y] = img[coordX][coordY]
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Image avant rotation")
    plt.subplot(1, 2, 2)
    plt.imshow(EmptyArray, cmap="gray")
    plt.title("Image après rotation")
    plt.show()

    return(EmptyArray)

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
    for i in range(0, len(N)):
        print(types[i], "with an order of ", int(N[i]))
    print(types[Nargmin], "with an order of ", int(Nmin), "is the minimal order Filter")

    return N[Nargmin], Wn[Nargmin]

def filterAndCreateElliFilter(N, Wn, img):
    num, den = signal.ellip(N, 0.2, 60, Wn, btype='low', analog=False, fs=1600)
    plt.title("Pôles et zéros du filtre calculé avec python")
    zplane.zplane(num,den)

    w, H = signal.freqz(num, den)

    plt.subplot(1, 2, 1)
    plt.plot(np.abs(H))
    plt.title("Module en fréquence du filtre")
    plt.subplot(1, 2, 2)
    plt.plot(np.angle(H))
    plt.title("Phase en Rad du filtre")
    plt.show()

    imgfilter = signal.lfilter(num, den, img)

    return (imgfilter)