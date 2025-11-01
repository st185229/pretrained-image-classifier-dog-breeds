#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Suresh Thomas
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
import os
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    results_dic = dict()
    
    # Get a list of image file names from the directory
    image_files = []
    try:
        for entry in os.listdir(image_dir):
            full_path = os.path.join(image_dir, entry)
            # Only consider files and exclude hidden files (like .DS_Store)
            if os.path.isfile(full_path) and not entry.startswith('.'):
                image_files.append(entry)
    except FileNotFoundError:
        print(f"Error: Directory not found at {image_dir}")
        return results_dic # Return empty dictionary on error
    except NotADirectoryError:
        print(f"Error: {image_dir} is not a directory")
        return results_dic # Return empty dictionary on error

    # Process each file name to extract the pet label
    for filename in image_files:
        # Convert filename to lowercase
        low_filename = filename.lower()
        
        # Split the filename by underscores to get potential words
        word_list_filename = low_filename.split("_")
        
        # Create pet_name starting as an empty string
        pet_name = ""
        
        # Loop through words in the filename and build the pet_name
        for word in word_list_filename:
            # Check if the word is alphabetic (to exclude numbers like '02259')
            if word.isalpha():
                pet_name += word + " "
        
        # Strip leading/trailing whitespace
        pet_name = pet_name.strip()
        
        # Add to results_dic
        # The key is the filename, and the value is a list containing the pet label
        if filename not in results_dic:
            results_dic[filename] = [pet_name]
        else:
            print(f"Warning: Duplicate file name found: {filename}")


    return results_dic
