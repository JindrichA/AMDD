import cv2
import matplotlib.pyplot as plt
import os
import csv
import matplotlib
matplotlib.use('TkAgg')
# Set the folder path
folder_path = 'Data'

# Open the CSV file for writing
with open('coordinates.csv', 'w', newline='') as csvfile:
    fieldnames = ['filename', 'x1', 'y1', 'x2', 'y2']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Loop over all images in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):

            # Load the image
            img = cv2.imread(os.path.join(folder_path, filename))

            h, w = img.shape[:2]
            # Resize the image to half its original size
            resized = cv2.resize(img, (w // 8, h // 8))
            # Display the image
            plt.imshow(resized)



            # Get user input using ginput
            pts = plt.ginput(n=2)

            # Write the coordinates to the CSV file
            writer.writerow({
                'filename': filename,
                'x1': pts[0][0],
                'y1': pts[0][1],
                'x2': pts[1][0],
                'y2': pts[1][1],
            })

# Close the window
cv2.destroyAllWindows()