import cv2 #Needs the opencv module to be installed
from matplotlib import pyplot as plt #Needs the matplotlib module to be installed
from skimage import morphology
import numpy as np

path = "./Hydrides/"
i = 1
imagelist = []

while i <= 16: #16 images, i values up to and including 16
    image = cv2.imread(path + "chu" + str(i) + ".jpg", 0) #Reads in the image. Do not change the original filenames.
    image_threshold =  cv2.adaptiveThreshold(image, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 1) #Conduct adaptive Gaussian Thresholding on the image
    
    image_threshold_inverted = np.invert(image_threshold)
    
    imagelist.append(image_threshold) #Add image to the image list
    
    
    
    clean_image_skimage = morphology.remove_small_holes(image_threshold, area_threshold = 175, connectivity = 1) #Conduct area-based thresholding to remove isolated pixels below a specified area threshold
    
    clean_image_skimage = np.uint8(clean_image_skimage) #Convert from boolean to uint8, otherwise opencv cannot process the array
    
    clean_image_skimage = np.invert(clean_image_skimage)
    
    element_open = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2)) #Define the structure size for the erosion treatment
    
    clean_image_open = cv2.morphologyEx(image_threshold_inverted, cv2.MORPH_OPEN, element_open) #Conduct an erosion and dilation treatment to reduce noise or small hydrides, in this case
    
    clean_image_open_combined = cv2.morphologyEx(clean_image_skimage, cv2.MORPH_OPEN, element_open)
    
    i += 1 
    
binary_value_list = [0,255]

@pytest.mark.filterwarnings("ignore::UserWarning")

for image in imagelist:
    for row in image:
        for pixel in row:
            assert pixel in binary_value_list, "Image is not fully binary, therefore not thresholded properly" #Tests if the image is fully binary or not.
