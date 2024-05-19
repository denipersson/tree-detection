import csv

# Define a set to hold unique image paths
unique_images = set()

# Open the CSV file and read data
with open('annotations.csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        image_path = row[0]
        unique_images.add(image_path)  # Add image path to the set (duplicates will be ignored)

# Print each unique image link
for image in unique_images:
    print(image)

# Optionally, save the unique image links to a new file
with open('unique_image_links.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['image_path'])
    for image in unique_images:
        writer.writerow([image])
