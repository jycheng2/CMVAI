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

directory = 'd:/CMVT9'

for dirname in os.listdir(directory):
        testdir=directory+"/"+dirname+"/positive_CL/"
        savedir=directory+"/"+dirname+"/positive/"
        t2 = sorted(glob.glob(testdir + "*"))
       

        for index,item in enumerate(t2):
                img = cv2.imread(item)

                for x in range(0,5):
                        y=360*(random.randint(0, 4)/4)
                        a=random.randint(-50, 50)
                        b=random.randint(-50, 50)
                        img2=rotate_image(img,y)
                        img2 = img2[106+a:406+a, 106+b:406+b]
                        fn=savedir+os.path.basename(item)+str(y)+'b.jpg'
                        cv2.imwrite(fn, img2)
                        
