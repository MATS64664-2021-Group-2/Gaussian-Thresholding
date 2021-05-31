"""
Cleans up the images to display connected hydrides and plots them side-by-side for comparison.

Inputs:

image_list - list of thresholded (binary images).

pure_image_list - list of non-thresholded images (for the sake of comparison).

Outputs:

None - (visual representation is enough in this case).

"""


import cv2 #Needs the opencv module to be installed
from matplotlib import pyplot as plt #Needs the matplotlib module to be installed
from skimage import morphology
import numpy as np

def image_clean_up(image_list, pure_image_list):
    j = 0
    for image in image_list:
        
        image_threshold_inverted = np.invert(image) #Inverts the thresholded image so the hydrides are white.
        
        clean_image_skimage = morphology.remove_small_holes(image, area_threshold = 175, connectivity = 1) #Conduct area-based thresholding to remove isolated pixels below a specified area threshold
    
        clean_image_skimage = np.invert(np.uint8(clean_image_skimage)) #Convert from boolean to uint8, otherwise opencv cannot process the array and invert the image so hydrides are white.
    
        element_open = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2)) #Define the structure size for the erosion treatment
    
        clean_image_open = cv2.morphologyEx(image_threshold_inverted, cv2.MORPH_OPEN, element_open) #Conduct an erosion and dilation treatment to reduce noise or small hydrides, in this case
    
        clean_image_skimage_combined = np.invert(morphology.remove_small_holes(np.invert(clean_image_open), area_threshold = 100, connectivity = 1)) #skimage processing on the opencv processed image.

        assert np.sum(clean_image_open == clean_image_skimage)/(len(image)*len(image[0]))*100 <= 95, "OpenCV and skimage processing produced an image that is 95% similar. Processing may be redundant."

        assert np.sum(clean_image_skimage_combined == clean_image_skimage)/(len(image)*len(image[0]))*100 <= 95, "OpenCV and skimage combined vs. skimage processing produced an image that is 95% similar. Processing may be redundant."

        assert np.sum(image_threshold_inverted == clean_image_open)/(len(image)*len(image[0]))*100 <= 95, "OpenCV processing has a 95% similarity to the original thresholded image. Processing may be redundant."
        
        assert np.sum(image_threshold_inverted == clean_image_skimage)/(len(image)*len(image[0]))*100 <= 95, "skimage processing has a 95% similarity to the original thresholded image. Processing may be redundant."
        
        assert np.sum(image_threshold_inverted == clean_image_skimage_combined)/(len(image)*len(image[0]))*100 <= 95, "OpenCV and skimage processing has a 95% similarity to the original thresholded image. Processing may be redundant."
        
        func, plots = plt.subplots(1,5, figsize =(40,40)) #Define subplot area
        
        plots[4].imshow(pure_image_list[j], "gray") #Plot everything for comparison and verification
        plots[3].imshow(clean_image_skimage_combined, "gray")
        plots[2].imshow(clean_image_skimage, "gray") 
        plots[1].imshow(clean_image_open, "gray")
        plots[0].imshow(image_threshold_inverted, "gray") 
        
        plots[4].axis("off") #Remove axes for increased clarity
        plots[3].axis("off") 
        plots[2].axis("off")
        plots[1].axis("off")
        plots[0].axis("off")
        
        plots[4].set_title("Original image", fontsize = "50") #Add titles for each processed image
        plots[3].set_title("OpenCV + skimage", fontsize = "50") 
        plots[2].set_title("skimage", fontsize = "50") 
        plots[1].set_title("OpenCV", fontsize = "50")
        plots[0].set_title("Gauss", fontsize = "50")
        
        plt.show() #Plot the images one by one for verification
        
        j += 1
