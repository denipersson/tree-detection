from PIL import Image
import os

def crop_to_square(image_path, output_path):
    with Image.open(image_path) as img:
        width, height = img.size
        new_size = min(width, height)

        left = (width - new_size) / 2
        top = (height - new_size) / 2
        right = (width + new_size) / 2
        bottom = (height + new_size) / 2

        img_cropped = img.crop((left, top, right, bottom))
        img_cropped.save(output_path)

# Get the absolute path to the directory the script is in
script_dir = os.path.abspath(os.path.dirname(__file__))

# Directory containing images
input_dir = os.path.join(script_dir, 'images')
output_dir = os.path.join(script_dir, 'cropped')

# Check and create output directory if not exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(f"Input Directory: {input_dir}")
print(f"Output Directory: {output_dir}")

# Crop all images in the directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        crop_to_square(image_path, output_path)
        print(f'Cropped {filename}')
