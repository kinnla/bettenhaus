
from PIL import Image
import os
import argparse

# Argument parser to accept an optional path to a specific image
parser = argparse.ArgumentParser(description='Scale images to a maximum width of 1920 pixels.')
parser.add_argument('--image_path', type=str, help='Optional path to a specific image to scale')
args = parser.parse_args()

def scale_image(image_path):
    with Image.open(image_path) as img:
        width, height = img.size

        # Check if the image width is greater than 1920 pixels
        if width > 1920:
            # Calculate the new height to maintain the aspect ratio
            new_height = int((1920 / width) * height)
            img = img.resize((1920, new_height), Image.LANCZOS)  # LANCZOS statt ANTIALIAS
            img.save(image_path)  # Overwrite the original image with the scaled version
            print(f'Scaled {image_path} to 1920x{new_height} pixels.')
        else:
            print(f'{image_path} is already within the required dimensions.')

# If a specific image path is provided, scale that image only
if args.image_path:
    if os.path.exists(args.image_path):
        scale_image(args.image_path)
    else:
        print(f'Error: The file {args.image_path} does not exist.')
else:
    # Search for all images in the current working directory
    for filename in os.listdir('.'):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            scale_image(filename)
