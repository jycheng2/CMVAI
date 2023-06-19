import os
import numpy as np
import cv2
import glob
import random

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

directory = 'd:/CMV3'

for dirname in os.listdir(directory):
        testdir=directory+"/"+dirname+"/positive_CL/"
        savedir=directory+"/"+dirname+"/positive/"
        t2 = sorted(glob.glob(testdir + "*"))
        for index,item in enumerate(t2):
                img = cv2.imread(item)

                for x in range(0,64):
                        y=360*(x/64)
                        img2=rotate_image(img,y)
                        img2 = img2[106:406, 106:406]
                        fn=savedir+os.path.basename(item)+str(y)+'.jpg'
                        cv2.imwrite(fn, img2)

        for index,item in enumerate(t2):
                img = cv2.imread(item)

                for x in range(0,128):
                        y=360*(x/128)
                        a=random.randint(-100, 100)
                        b=random.randint(-100, 100)
                        img2=rotate_image(img,y)
                        img2 = img2[106+a:406+a, 106+b:406+b]
                        fn=savedir+os.path.basename(item)+str(y)+'b.jpg'
                        cv2.imwrite(fn, img2)
                        
