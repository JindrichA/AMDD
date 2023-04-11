import os
import 
# Folder with original images
data_path = 'data/original_images'

# Creating a list of all images in the folder
list_of_all_images = os.listdir(data_path)

# Looping through all images in the folder
for i in range(len(list_of_all_images)):
    # Reading the image
    image = cv2.imread(data_path + '/' + list_of_all_images[i], cv2.IMREAD_COLOR)
    # Resizing the image
    image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
    # Saving the image
    cv2.imwrite('data/resized_images/' + list_of_all_images[i], image)



