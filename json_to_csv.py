import json
import csv

# Load the JSON data from the file
with open('exported_data.json', 'r') as file:
    data = json.load(file)

# Open a CSV file to write to
with open('annotations.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['image_path', 'xmin', 'ymin', 'xmax', 'ymax', 'label'])

    # Process each entry in the JSON data
    for item in data:
        image_path = item['data_row']['row_data']  # Getting the image URL
        for annotation in item['projects']['clw7x348k0314072q32swa45r']['labels'][0]['annotations']['objects']:
            xmin = annotation['bounding_box']['left']
            ymin = annotation['bounding_box']['top']
            xmax = xmin + annotation['bounding_box']['width']
            ymax = ymin + annotation['bounding_box']['height']
            label = annotation['name']  # Assuming the 'name' field contains the label

            # Write the row to the CSV
            writer.writerow([image_path, xmin, ymin, xmax, ymax, label])
