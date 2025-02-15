import cv2
import numpy as np

def main():
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

        # Convert the frame to grayscale.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise.
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Perform Canny edge detection.
        edges = cv2.Canny(blurred, 100, 200)
        
        # Experiment with Parameters: Adjust blur kernels 
        # ((5, 5), (7, 7), etc.) and Canny thresholds 
        # (e.g., (50, 150), (100, 200)) to see how they 
        # affect the edge detection results.
        
        # Display the original (grayscale) and the edges.
        cv2.imshow('Original (Grayscale)', gray)
        cv2.imshow('Edges', edges)

        # Press 'q' to quit.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera resource and close windows.
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
