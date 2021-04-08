import cv2 #Needs the opencv module to be installed
from matplotlib import pyplot as plt #Needs the matplotlib module to be installed


path =  #Enter the path of the directory, which contains all the images to be thresholded. 
i = 1 #Integer to keep track of the used images in the while loop
imagelist = [] #List to contain all the processed images

while i <= 16: #16 images, i values up to and including 16
    image = cv2.imread(path + "\chu" + str(i) + ".jpg", 0) #Reads in the image. Do not change the original filenames.
    image_threshold =  cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 1) #Conduct adaptive Gaussian Thresholding on the image
    imagelist.append(image_threshold) #Add image to the image list
    plt.imshow(image_threshold, "gray")
    plt.show() #Plot the images one by one for verification
    i += 1 
    
