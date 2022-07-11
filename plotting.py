from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from PIL import Image
from numpy import append
import matplotlib.pyplot as plt
import os 
from os import listdir
import matplotlib.image as mpimg
from matplotlib import pylab as pl
import numpy as np
from natsort import os_sorted
import math

path = "./frames"
outpath = './outframes'

fig = pyplot.figure()
axis = fig.add_subplot(1, 1, 1, projection="3d") # 3D plot with scalar values in each axis


for f in os_sorted(os.listdir(path)):
    if f.endswith(".jpg"):
        #image = Image.open(path + '/' + f).convert('L')
        print(f)
        im = Image.open(os.path.join(path, f)).convert('L')
        z   = np.asarray(im)
        mydata = z[::1,::1]
        fig = pl.figure(facecolor='w')
        ax1 = fig.add_subplot(1,2,1)
        im = ax1.imshow(mydata,interpolation='nearest',cmap=pl.cm.jet)
        ax1.set_title('2D')

        ax2 = fig.add_subplot(1,2,2,projection='3d')
        x,y = np.mgrid[:mydata.shape[0],:mydata.shape[1]]
        ax2.plot_surface(x,y,mydata,cmap=pl.cm.jet,rstride=1,cstride=1,linewidth=0.,antialiased=False)
        ax2.set_title('3D')
        ax2.set_zlim3d(0,100)
        #pl.show()
        save_name = os.path.join(outpath, os.path.basename(f)+'.jpg')
        pyplot.savefig(save_name)
