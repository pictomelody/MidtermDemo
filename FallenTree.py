import sys
sys.path.append('C\Annie\Python2.7\Lib\site-packages')
#from os import getcwd

import numpy as np #image manipulation
import cv2 #image manipulation
import mingus.extra.lilypond as Lilypond #music manipulation
import mingus.core.notes as notes #music manipulation
import musicAndColor as musc #image to music data
import Music as muscno #bass chords
from melopy import Melopy #sounds
from averageColor import averageColorGrid #image data
from averageColor import ImageDimensions #image data
from cvHistExample import showHistogram #image data
from histToNote import showMeTheNote #melody

def Timber(filename):
    song_melopy = Melopy(filename)
    #print (getcwd())

    with open('D:/Annie/Code/pictoMelody/togetherCodefest/' + filename + '.mlp','r') as f:
        f.seek(0)
        song_melopy.parse(f.read())

    song_melopy.render()

image_filename = raw_input("Enter the mlp filename (w/o .mlp extension): ")
Timber(image_filename)
