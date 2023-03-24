import cv2
import os
import json

def calc_info(metadata_filename, output_filename):

    # Load JSON file
    with open(metadata_filename) as f:
        data = json.load(f)

    # Set path to images
    path = 'dataverse_files/'

    # Loop through each image in JSON file
    for painting in data:
        filename = painting['Filename']
        title = painting['Title']
        author = painting['Author']
        img_path = os.path.join(path, filename)

        # Load image with OpenCV
        img = cv2.imread(img_path)

        if img is None:
            print('Could not read image: {} by {}'.format(title, author))
            continue

        # Convert image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Calculate contrast using standard deviation of pixel intensities
        contrast = gray.std()

        # Convert image to HSV color space
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Calculate mean saturation and brightness
        saturation = cv2.mean(hsv[:,:,1])[0]
        brightness = cv2.mean(hsv[:,:,2])[0]

        # Calculate dominant hue
        hue_range = [0, 180]  # Range for hue values in OpenCV
        hue_hist = cv2.calcHist([hsv], [0], None, [180], hue_range)
        dominant_hue = hue_hist.argmax()

        # Append values to list
        painting['contrast'] = contrast
        painting['saturation'] = saturation
        painting['brightness'] = brightness
        painting['dominant_hue'] = int(dominant_hue)

    # Save updated JSON file
    with open(output_filename, 'w') as f:
        json.dump(data, f, indent=4)

calc_info('turner.json', 'turner_contrast.json')
calc_info('monet.json', 'monet_contrast.json')
