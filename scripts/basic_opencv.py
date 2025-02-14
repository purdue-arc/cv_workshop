import cv2
import numpy as np

def main():
    # Open the default camera (device index 0).
    cap = cv2.VideoCapture(-1)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read frame from camera.")
            break

        # Convert to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Display the frames (color and grayscale).
        cv2.imshow('Camera Feed (Color)', frame)
        cv2.imshow('Camera Feed (Grayscale)', gray)

        # Press 'q' to quit.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera resource and close windows.
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()