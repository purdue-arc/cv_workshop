import cv2
import numpy as np
from ultralytics import YOLO

def main():
    # Load a YOLOv8 model (e.g. "yolov8n.pt" for the Nano model).
    # You can choose different variants (yolov8s.pt, yolov8m.pt, etc.) depending on your needs.
    model = YOLO("yolov8n.pt")
    
    # Open the default camera (device index 0).
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read frame from camera.")
            break

        # Perform inference on the current frame
        results = model(frame)  # By default, runs on CPU. Add 'device=0' or similar if you have a GPU.

        # The 'results' object is a list; usually we only have one item for a single image/frame.
        detections = results[0]  # The first (and only) result

        # Each detection has .boxes, which contains bounding boxes, confidence scores, and class IDs
        # For each box:
        for box in detections.boxes:
            # box.xyxy: [x1, y1, x2, y2]
            # box.cls: class index
            # box.conf: confidence
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
            cls_index = int(box.cls[0].item())
            confidence = float(box.conf[0].item())

            # Get class name using model.names (a list of class labels).
            class_name = model.names[cls_index]

            # Convert to integer for drawing
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # Draw bounding box
            color = (0, 255, 0)  # green, can be changed or randomized
            thickness = 2
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)

            # Display label (class name + confidence)
            label = f"{class_name} {confidence:.2f}"
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                color,
                thickness=1
            )

        # Show the annotated frame
        cv2.imshow("YOLOv8 Detection", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera resource and close windows.
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
