from deepforest import main
import matplotlib.pyplot as plt

# Initialize the model
model = main.deepforest()
model.use_release()

# Load your image and predict
image_path = 'images/1.png'
# Predict tree crowns without plotting
boxes = model.predict_image(path=image_path, return_plot=False)

# Print the number of bounding boxes
print("Number of bounding boxes:", len(boxes))

# Predict again with plotting
predictions_plot = model.predict_image(path=image_path, return_plot=True, color=(0, 0, 255))

# Convert BGR to RGB for matplotlib
predictions_rgb = predictions_plot[:, :, ::-1]

# Display the predictions
plt.figure(figsize=(10, 10))
plt.imshow(predictions_rgb)
plt.show()
