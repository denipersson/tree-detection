from deepforest import main
import torch
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
import os

# Initialize and load the pre-trained model
model = main.deepforest()
model.use_release()

# List of image paths
image_paths = [
    '1.JPG',
    '2.JPG',
    '3.JPG',
    '4.JPG',
    '5.JPG'
]

# Create a result directory if it does not exist
os.makedirs('result', exist_ok=True)

# Initialize a list to keep track of image names and bounding box counts
results_summary = []

for image_path in image_paths:
    try:
        # Load image using OpenCV
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image file not found: {image_path}")

        # Convert BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Predict bounding boxes without plotting
        boxes = model.predict_image(image=image_rgb, return_plot=False)
        if boxes is None or boxes.empty:
            raise ValueError("No bounding boxes detected.")

        # Create a matplotlib figure to plot
        plt.figure(figsize=(10, 10))
        ax = plt.gca()
        plt.imshow(image_rgb)

        # Draw bounding boxes on the image
        for idx, row in boxes.iterrows():
            rect = patches.Rectangle(
                (row['xmin'], row['ymin']), row['xmax'] - row['xmin'], row['ymax'] - row['ymin'],
                linewidth=2, edgecolor='yellow', facecolor='none'
            )
            ax.add_patch(rect)

        # Save the plotted image
        result_image_path = f"result/RESULT_{os.path.basename(image_path)}"
        plt.axis('off')
        plt.savefig(result_image_path, bbox_inches='tight')
        plt.close()

        # Record the result
        results_summary.append(f"{os.path.basename(image_path)}: {len(boxes)}")

    except Exception as e:
        print(f"Error with {image_path}: {e}")

# Write the results summary to a text file
with open('result/summary.txt', 'w') as file:
    for result in results_summary:
        file.write(result + '\n')

print("Processing complete. Check the 'result' folder for outputs and summary.")
