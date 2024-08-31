import cv2
from ultralytics import YOLO
import pyttsx3

# Load the trained model
model = YOLO('trained_model3.pt')  # Replace with your model path

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

last_detected_sign = None

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error reading frame from webcam.")
        break

    # Perform detection
    results = model(frame)

    # Extract detected sign
    current_sign = None
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            label = model.names[class_id]
            current_sign = label
            break  # Break after detecting the first sign

    if current_sign and current_sign != last_detected_sign:
        speak(current_sign)
        last_detected_sign = current_sign

    # Draw bounding boxes and labels on the frame
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = float(box.conf)  # Convert tensor to float
            class_id = int(box.cls)
            label = model.names[class_id]
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f'{label} ({confidence:.2f})', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('ISL Detection', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
