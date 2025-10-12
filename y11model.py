import ultralytics
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolo11n-cls.pt")

# Train the model on the dataset
results = model.train(data="./dataset", epochs=20)

# Export the trained model to a format that can be used for inference or deployment
model.export()

# Run predictions on the images in the folder, save the results as images or outputs
model.predict('./dataset/test', save=True)

