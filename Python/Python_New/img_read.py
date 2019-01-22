# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:52:09 2019

@author: athakre
"""

# Python program to read image using OpenCV 

# importing OpenCV(cv2) module 
import cv2 

# Save image in set directory 
# Read RGB image 
img = cv2.imread('test.jpg') 

# Output img with window name as 'image' 
cv2.imshow('image', img) 

# Maintain output window utill 
# user presses a key 
cv2.waitKey(0)		 

# Destroying present windows on screen 
cv2.destroyAllWindows() 
