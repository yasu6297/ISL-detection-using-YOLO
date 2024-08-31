from ultralytics import YOLO

# Load the YOLO model
model = YOLO('yolov8s.pt')  # Use the pre-trained YOLOv8n model as a starting point

# Train the model
model.train(
    data='C:/Users/itzya/OneDrive/Desktop/ISL using YOLOv5.v7i.yolov8-obb/data.yaml',  # Path to the data.yaml file
    epochs=10,  # Number of training epochs
    imgsz=640,  # Image size
    batch=16,  # Batch size
    name='yolov8n_sign_language',  # Name of the training session
    verbose=True  # Verbose output to monitor training progress
)

# Save the trained model
try:
    model.save('trained_model3.pt')
    print("Model saved successfully.")
except Exception as e:
    print(f"An error occurred while saving the model: {e}")
