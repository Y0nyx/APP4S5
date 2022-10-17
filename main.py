import matplotlib.pyplot as plt
import numpy as np
import PictureManager
import Compression
import zplane
from scipy import signal

if __name__ == '__main__':
    #abberation
    num = np.poly([0.9*np.exp(np.pi/2j), 0.9*np.exp(-np.pi/2j), 0.95*np.exp(np.pi/8j), 0.95*np.exp(-np.pi/8j)])
    den = np.poly([0, 0.80, -0.99, -0.99])
    img = np.load("img\\image_complete.npy")

    # La fonction es stable car les pôles sont dans le cercle unitaire
    plt.title("Pôles et zéros de la fonction de transfert à appliquer")
    zplane.zplane(den, num)

    imageSansAbberation = PictureManager.revertAbberation(img, num, den)

    #rotation
    imageRotater = PictureManager.rotation90degree(imageSansAbberation)

    #Filtre en utilisant la transformation bilinéaire
    a = 0.418163346
    zeros = np.roots([a, 2*a, a])
    poles = np.roots([1, 0.462937924, 0.209715358])
    num2 = np.poly(zeros)
    den2 = np.poly(poles)

    w, H = signal.freqz(num2, den2)
    plt.subplot(1, 2, 1)
    plt.plot(np.abs(H))
    plt.title("Module en fréquence du filtre utilisant la technique bilinéaire")
    plt.subplot(1, 2, 2)
    plt.plot(np.angle(H))
    plt.title("Phase en Rad du filtre utilisant la technique bilinéaire")
    plt.show()
    # La fonction es stable car les pôles sont dans le cercle unitaire
    plt.title("Pôles et zéros de la fonction du filtre calculé à la main")
    zplane.zplane(num2, den2)

    imgFiltreBilineaire = signal.lfilter(num2, den2, imageRotater)
    # Comparaison différent type de filtre et filtre du bruit
    N, Wn = PictureManager.ComparaisonFiltre(500, 750, 0.2, 60, 1600)
    imageFiltre = PictureManager.filterAndCreateElliFilter(N, Wn, imageRotater)

    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Image avec bruit")
    plt.subplot(1, 3, 2)
    plt.imshow(imageFiltre, cmap="gray")
    plt.title("Image sans bruit utilisant python")
    plt.subplot(1, 3, 3)
    plt.imshow(imgFiltreBilineaire, cmap="gray")
    plt.title("Image sans bruit utilisant la technique bilinéaire")
    plt.show()

    #Compression
    Compression.compression(imageFiltre, 50)
    Compression.compression(imageFiltre, 70)




