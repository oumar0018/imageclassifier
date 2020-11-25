from os import listdir

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
     results_dic = dict()

     # Get the file names from the list
     pet_file_names = listdir(image_dir)

     pet_labels = get_labels(pet_file_names)

     for idx in range(0, len(pet_file_names), 1):
         if pet_file_names[idx] not in results_dic:
             results_dic[pet_file_names[idx]] = [pet_labels[idx]]
         else:
             print("** Warning: Key=", pet_file_names[idx], 
                "already exists in results_dic with value =", 
                results_dic[pet_file_names[idx]])
     # Replace None with the results_dic dictionary that you created with this
     # function
     return results_dic

def get_labels(name_list):

    # Initialize the list of file_names
    list_of_labels = []

    for name in name_list:
        # Get the label of each name
        pet_label = get_label(name)
        # Add the label to the list
        list_of_labels.append(pet_label)

    return list_of_labels


def get_label(name):
    # Make name lower case
    name = name.lower()

    # separate into words 
    words = name.split("_")

    # Initialize pet label variable 
    pet_label = ""
    for word in words:
        if word.isalpha():
            pet_label += word + " "
    # remove white spaces start/end points
    pet_label = pet_label.strip()

    return pet_label
