import numpy as np
import matplotlib.image as mpimg
import PictureManager

if __name__ == '__main__':
    # abberation
    num = np.poly([0.9*np.exp(np.pi/2j), 0.9*np.exp(-np.pi/2j), 0.95*np.exp(np.pi/8j), 0.95*np.exp(-np.pi/8j)])
    den = np.poly([-0.99, -0.99, 0.8])
    img = np.load("img\\goldhill_aberrations.npy")
    PictureManager.revertAbberation(img, num, den)

    #rotation
    img_color = mpimg.imread("img\\goldhill_rotate.png")
    img = np.mean(img_color, -1)
    PictureManager.rotation90degree(img)

