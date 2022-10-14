import numpy as np
import PictureManager

if __name__ == '__main__':
    num = np.poly([0.9*np.exp(np.pi/2j), 0.9*np.exp(-np.pi/2j), 0.95*np.exp(np.pi/8j), 0.95*np.exp(-np.pi/8j)])
    den = np.poly([-0.99, -0.99, 0.8])
    img = np.load("img\\goldhill_aberrations.npy")
    img = PictureManager.revertAbberation(img, num, den)

