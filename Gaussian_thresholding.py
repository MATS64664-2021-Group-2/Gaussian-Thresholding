"""
Thresholds images to binary for ease of processing.

Inputs:

path - directory path for images

Outputs:

imagelist - list of thresholded images (list of numpy arrays)

pure_image_list - list of unthresholded images (for subsequent plotting and comparison of results)
"""

import cv2

def Gaussian_thresholding(path):
    i = 1 #Integer to keep track of the used images in the while loop
    imagelist = [] #List to contain all the processed images   
    pure_imagelist = [] #List to contain all the unprocessed images
    while i <= image_count(path): #16 images, i values up to and including 16
        
        image = cv2.imread(path + "chu" + str(i) + ".jpg", 0) #Reads in the image. Do not change the original filenames.
        image_threshold =  cv2.adaptiveThreshold(image, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 1) #Conduct adaptive Gaussian Thresholding on the image
        
        pure_imagelist.append(image) #Add the original images to the unprocessed image list.
        imagelist.append(image_threshold) #Add image to the image list
        i += 1
        
    return imagelist, pure_imagelist #Returns both lists
