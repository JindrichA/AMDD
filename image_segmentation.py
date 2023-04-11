import cv2
import os
import csv
import glob

data_path = 'data/original_images'

number_of_segments = 10

# Creating a list of all images in the folder
list_of_all_images = os.listdir(data_path)

x1_list = []
y1_list = []
x2_list = []
y2_list = []



def cut_images(image, x_coord_1, x_coord_2, fields):
    # Cut the image between the two x-coordinates
    cropped_image = image[:, x_coord_1:x_coord_2]

    # Calculate the width of each field
    field_width = (x_coord_2 - x_coord_1) // fields

    # Create a list to store the field images
    field_images = []

    # Cut the cropped image into the specified number of fields
    for i in range(fields):
        field_image = cropped_image[:, i * field_width:(i + 1) * field_width]
        field_images.append(field_image)

    return field_images


def draw_lines(image, x_coord_1, x_coord_2, fields, color, thickness):
    # Define the start and end points of the first and last lines
    start_point_1 = (x_coord_1, 0)  # top of the image
    end_point_1 = (x_coord_1, image.shape[0])  # bottom of the image
    start_point_2 = (x_coord_2, 0)  # top of the image
    end_point_2 = (x_coord_2, image.shape[0])  # bottom of the image

    # Calculate the x coordinate increment for the remaining lines
    x_increment = (x_coord_2 - x_coord_1) / (fields)

    # Draw the first and last lines
    cv2.line(image, start_point_1, end_point_1, color, thickness)
    cv2.line(image, start_point_2, end_point_2, color, thickness)

    # Save a part of image with boundaries defined by the coordinates



    # Draw the remaining lines
    for i in range(fields):
        x_coord = int(x_coord_1 + (i + 1) * x_increment)
        start_point = (x_coord, 0)
        end_point = (x_coord, image.shape[0])
        cv2.line(image, start_point, end_point, color, thickness)

# load a files with coordinates of the object
# REPLACE WITH THE NEW ONE IF YOU WANT TO CHANGE THE COORDINATES

with open('coordinates_save.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Get the coordinates of the object
        x1 = (row['x1'])
        y1 = (row['y1'])
        x2 = (row['x2'])
        y2 = (row['y2'])

        # Convert the coordinates to integers
        x1_list.append(8*int(float(x1)))
        y1_list.append(8*int(float(y1)))
        x2_list.append(8*int(float(x2)))
        y2_list.append(8*int(float(y2)))

for i in range(len(list_of_all_images)):

    image = cv2.imread(data_path+'/'+list_of_all_images[i], cv2.IMREAD_COLOR)

    draw_lines(image, x1_list[i], x2_list[i], number_of_segments, (0, 0, 255), 10)
    height, width, channels = image.shape
    new_width = int(image.shape[1] / 8)
    new_height = int(image.shape[0] / 8)
    resized_img = cv2.resize(image, (new_width, new_height))
    cv2.imshow('image', resized_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()


    fields = number_of_segments

    # Cut the image into fields and store them in a list
    temp_folder_path = 'data/segmented_images/'+list_of_all_images[i]
    if not os.path.exists(temp_folder_path):
        # Create the folder
        os.makedirs(temp_folder_path)
        print(f"Folder '{temp_folder_path}' created.")
    else:
        print(f"Folder '{temp_folder_path}' already exists.")
        image_extensions = ["*.jpg", "*.jpeg", "*.png", "*.bmp"]

        # Iterate through the image extensions and delete the images
        for ext in image_extensions:
            image_files = glob.glob(os.path.join(temp_folder_path, ext))
            for image_file in image_files:
                os.remove(image_file)
                print(f"Deleted '{image_file}'")

    field_images = cut_images(image, x1_list[i], x2_list[i], fields)
    # Save the field images
    for ii, field_image in enumerate(field_images):
        cv2.imwrite(temp_folder_path+f"/output_image_{ii + 1}.jpg", field_image)


print('Finish')

#







