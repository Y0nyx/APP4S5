import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import signal
import zplane
def revertAbberation(img, num, den):
    # La fonction es stable car les pôles sont dans le cercle unitaire
    zplane.zplane(den, num)

    # Pour comparer, enregistrer l'image avec l'abberation
    mpimg.imsave("img\\gold_abberations.png", arr=img)

    # Filtre et enregistre l'image finale
    FiltedImg = signal.lfilter(den, num, img)
    mpimg.imsave("imgFinale\\gold_abberations_Finale.png", arr=FiltedImg)

def rotation90degree (img):
    #lecture nécessaire

