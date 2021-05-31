"""
Count the number of images within the specified folder.

Inputs:

path - folder path that will be counted.

Outputs:

len(images) - the number of files within the directory specified in "path". (Counts all images, so the folder must be empty of other files.)
"""


import os

def image_count(path): #Counts the amount of images for an automated count for the following while loop.
    for root, directories, images in os.walk(path): #Walk the path and get the directories and filelist.
        return len(images) #Return the number of filer in the specified path, this only works if there are no excess files in the directory.
