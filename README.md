# Image-Thresholding
Code for the image thresholding task

Includes adaptive Gaussian thresholding and noise removal techniques with comparison of methods.

Main output is $FILE$, which consists of three functions:

## image_count:

Count the number of images within the specified folder.

Input:
path - folder path that will be counted.

Output:
len(images) - the number of files within the directory specified in "path". (Counts all images, so the folder must be empty of other files.)

## Gaussian_thresholding:

Thresholds images to binary for ease of processing.

Input:
path - directory path for images

Outputs:
imagelist - list of thresholded images (list of numpy arrays)
pure_image_list - list of unthresholded images (for subsequent plotting and comparison of results)

## image_clean_up:

Cleans up the images to display connected hydrides and plots them side-by-side for comparison.

Inputs:
image_list - list of thresholded (binary images).
pure_image_list - list of non-thresholded images (for the sake of comparison).

Output:
None - (visual representation is enough in this case, as the results could not be used for further analysis).
