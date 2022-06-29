import cv2
import os 
from os import listdir

outpath = './frames'
vidcap = cv2.VideoCapture('octopus.mp4')
success,image = vidcap.read()
count = 0
while success:
  #save_name = os.path.join(outpath + '.jpg')
  cv2.imwrite("frame%d.jpg" % count, image)   # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1