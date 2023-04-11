import os
import cv2
import numpy as np
# Folder with original images
data_path = 'data/original_images'

# Creating a list of all images in the folder
list_of_all_images = os.listdir(data_path)

# Looping through all images in the folder
for i in range(len(list_of_all_images)):
    # Reading the image
    image = cv2.imread(data_path + '/' + list_of_all_images[i], cv2.IMREAD_COLOR)

    # Getting the image details
    current_image = list_of_all_images[i]
    image_path = data_path+'/'+current_image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    height, width, channels = image.shape
    # print the name of file and its size
    print(current_image, height, width, channels)

    ## Basic image preprocessing
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Blur the image to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Apply edge detection method on the image
    v = np.median(blur)
    # Set the lower and upper thresholds as a fraction of the median
    lower = int(max(0, (1.0 - 0.33) * v))
    upper = int(min(255, (1.0 + 0.33) * v))
    edges = cv2.Canny(blur, lower, upper)
    # This returns an array of r and theta values
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    # The below for loop runs till r and theta values
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw the contours on the original image
    contour_image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
    # Display the image with the contours (optional)
    resized_image = cv2.resize(contour_image, (int(width/8), int(height/8)))
    # Save the image
    cv2.imwrite('data/contour_images/' + current_image[:-4]+'_countour.jpg', contour_image)
    # cv2.imshow('Contours', resized_image)
    # cv2.waitKey(1000)
    cv2.destroyAllWindows()








