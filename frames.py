import cv2
import os 
from os import listdir

outpath = './frames'
vidcap = cv2.VideoCapture('output.mp4')
success,image = vidcap.read()
count = 0
while success:
  vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*100))    # added this line 
  success,image = vidcap.read()
  print ('Read a new frame: ', success)
  cv2.imwrite( outpath + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
  count = count + 1
