import sys

sys.path.append('C\Annie\Python2.7\Lib\site-packages')

import numpy as np
import cv2
import musicAndColor as musc
import Music as muscno
from averageColor import averageColorGrid
from averageColor import ImageDimensions
from cvHistExample import showHistogram

#Global variables
image_filename = "Horizon.png"
avg_image_filename = "Average-Color.png"
avgcolor_img = ""
n = 5

#x_img = cv2.imread(x_image)
print("Average Color Array: ")
print(averageColorGrid(image_filename, n))

img = cv2.imread(image_filename)
img_dim = ImageDimensions(img, n)
img_avg = cv2.imread(avg_image_filename)
most_avg = musc.more_average(img_avg)
octave = musc.pick_octave(img_avg)
key = musc.pick_key(most_avg)
if musc.pick_major(img_avg, n) == "major":
    major = True
else:
    major = False

print("most_avg: ", most_avg)
print("Music Info: ")
print("Octave: ", octave)
print("Major: ", major)
print("Key: ", key)
print("Notes: ")

track = muscno.create_random_track('C', major)

print(track)
"""
print("Graphs: ")
#Graphs for each average color box
for i in xrange(n):
    y1 = i*img_dim.height_box #upper limit of box height
    y2 = y1+img_dim.height_box
    for j in xrange(n):
        x1 = j*img_dim.width_box
        x2 = x1+img_dim.width_box
        img_box = img[x1:x2, y1:y2]
        showHistogram(img_box, "BGR")
"""
