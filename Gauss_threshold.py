import cv2 #Needs the opencv module to be installed
from matplotlib import pyplot as plt #Needs the matplotlib module to be installed
from skimage import morphology
import numpy as np

path =  r"C:\Users\Enn\Documents\CDT projekt\Coursework\Hydrides" #Enter the path of the directory, which contains all the images to be thresholded. 
i = 1 #Integer to keep track of the used images in the while loop
imagelist = [] #List to contain all the processed images   
    

while i <= 16: #16 images, i values up to and including 16
    image = cv2.imread(path + "\chu" + str(i) + ".jpg", 0) #Reads in the image. Do not change the original filenames.
    image_threshold =  cv2.adaptiveThreshold(image, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 1) #Conduct adaptive Gaussian Thresholding on the image
    
    image_threshold_inverted = np.invert(image_threshold)
    
    imagelist.append(image_threshold) #Add image to the image list
    
    
    
    clean_image_skimage = morphology.remove_small_holes(image_threshold, area_threshold = 175, connectivity = 1) #Conduct area-based thresholding to remove isolated pixels below a specified area threshold
    
    clean_image_skimage = np.uint8(clean_image_skimage) #Convert from boolean to uint8, otherwise opencv cannot process the array
    
    clean_image_skimage = np.invert(clean_image_skimage)
    
    element_open = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2)) #Define the structure size for the erosion treatment
    
    clean_image_open = cv2.morphologyEx(image_threshold_inverted, cv2.MORPH_OPEN, element_open) #Conduct an erosion and dilation treatment to reduce noise or small hydrides, in this case
    
    clean_image_open_combined = cv2.morphologyEx(clean_image_skimage, cv2.MORPH_OPEN, element_open)
    
    print("Similarity between opencv and skimage morphology processing: " + str(round(np.sum(clean_image_open == clean_image_skimage)/(len(image)*len(image[0]))*100, 1)) + "%")
    print("Similarity between skimage and opencv morphology processing combined vs. skimage: " + str(round(np.sum(clean_image_open_combined == clean_image_skimage)/(len(image)*len(image[0]))*100, 1)) + "%")    
    
    #Display the fact that all the processed images are different, hence they all deserve separate testing and subsequent analysis.
    

    
    func, plots = plt.subplots(1,4, figsize =(45,45)) #Define subplot area
    
    
    plots[3].imshow(clean_image_open_combined, "gray") #Plot everything for comparison and verification
    plots[2].imshow(clean_image_skimage, "gray") 
    plots[1].imshow(clean_image_open, "gray")
    plots[0].imshow(image_threshold_inverted, "gray") 
    
    
    plots[3].axis("off") #Remove axes for increased clarity
    plots[2].axis("off")
    plots[1].axis("off")
    plots[0].axis("off")
    
    
    plots[3].title.set_text("OpenCV + skimage") #Add titles for each processed image
    plots[2].title.set_text("skimage")
    plots[1].title.set_text("OpenCV")
    plots[0].title.set_text("Gauss ")
    
    plt.show() #Plot the images one by one for verification
    i += 1 
