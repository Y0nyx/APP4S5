import numpy as np
import matplotlib.image as mpimg
import PictureManager
import Compression
import zplane

if __name__ == '__main__':
    # abberation
    num = np.poly([0.9*np.exp(np.pi/2j), 0.9*np.exp(-np.pi/2j), 0.95*np.exp(np.pi/8j), 0.95*np.exp(-np.pi/8j)])
    den = np.poly([-0.99, -0.99, 0.8])
    img = np.load("img\\image_complete.npy")
    PictureManager.revertAbberation(img, num, den)

    #rotation
    #img_color = mpimg.imread("img\\goldhill_rotate.png")
    #img = np.mean(img_color, -1)
    PictureManager.rotation90degree(img)

    #Filtre en utilisant la transformation bilinéaire
    a = 0.418163346
    num2 = np.roots([a, 2*a, a])
    den2 = np.roots([1, 0.462937924, 0.209715358])
    # La fonction es stable car les pôles sont dans le cercle unitaire
    #zplane.zplane(num2, den2)

    # Comparaison différent type de filtre et filtre du bruit
    #img = np.load("img\\goldhill_aberrations.npy")
    #mpimg.imsave("img\\goldhill_bruit.png", arr=img, cmap="gray")
    N, Wn = PictureManager.ComparaisonFiltre(500, 750, 0.2, 60, 1600)
    PictureManager.filterAndCreateElliFilter(N, Wn, img)

    #Compression
    Compression.compression(img, 70)




