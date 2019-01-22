# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:31:09 2019

@author: athakre
"""
# Python code to reading an image using OpenCV 
import numpy as np 
import cv2 

# You can give path to the 
# image as first argument 
img = cv2.imread('cc.jpg', 0) 

# will show the image in a window 
cv2.imshow('image', img) 
k = cv2.waitKey(0) & 0xFF

# wait for ESC key to exit 
if k == 27: 
	cv2.destroyAllWindows() 
	
# wait for 's' key to save and exit 
elif k == ord('s'): 
	cv2.imwrite('grayscale_output.png',img) 
	cv2.destroyAllWindows() 
