import cv2 #Needs the opencv module to be installed
from matplotlib import pyplot as plt #Needs the matplotlib module to be installed


path =  #Enter the path of the directory, which contains all the images to be thresholded. 
i = 1 #Integer to keep track of the used images in the while loop
imagelist = [] #List to contain all the processed images

while i <= 16: #16 images, i values up to and including 16
    image = cv2.imread(path + "\chu" + str(i) + ".jpg", 0) #Reads in the image. Do not change the original filenames.
    image_threshold =  cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 1) #Conduct adaptive Gaussian Thresholding on the image
    imagelist.append(image_threshold) #Add image to the image list
    
    clean_image_skimage = morphology.remove_small_holes(image_threshold, area_threshold = 50, connectivity = 2) #Conduct area-based thresholding to remove isolated pixels below a specified area threshold
    clean_image_skimage_points = morphology.remove_small_objects(clean_image_skimage, min_size = 1000, connectivity = 2) #Conduct length-based thresholding to remove any leftover pixels from the previous thresholding
    clean_image_skimage = np.uint8(clean_image_skimage) #Convert from boolean to uint8, otherwise opencv cannot process the array
    
    
    element_open = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2)) #Define the structure size for the erosion treatment
    
    clean_image_open = cv2.morphologyEx(clean_image_skimage, cv2.MORPH_OPEN, element_open) #Conduct an erosion and dilation treatment to reduce noise or small hydrides, in this case
    
    print("Similarity between skimage and opencv morphology processing: " + str(round(np.sum(clean_image_open == clean_image_skimage)/(len(image)*len(image[0]))*100, 1)) + "%")
    
    #Show that the opencv morphology further treats the image, as they look very similar qualitatively
    
    func, plots = plt.subplots(1,3)
    plots[2].imshow(clean_image_skimage, "gray") #Plot everything for comparison and verification
    plots[1].imshow(clean_image_open, "gray")
    plots[0].imshow(image_threshold, "gray") 
    
    plt.show() #Plot the images one by one for verification
    i += 1 
    
