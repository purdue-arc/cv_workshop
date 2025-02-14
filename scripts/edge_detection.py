import cv2
import numpy as np

def main():
    # Load an image
    # Replace 'path/to/image.jpg' with a valid image path
    img = cv2.imread('path/to/image.jpg', cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error: Image not found or unable to open.")
        return

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(img, (5, 5), 0)

    # Perform Canny edge detection
    edges = cv2.Canny(blurred, 100, 200)

    # Display original and edges
    cv2.imshow('Original (Grayscale)', img)
    cv2.imshow('Edges', edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the resulting edge-detected image
    cv2.imwrite('edges_output.jpg', edges)
    print("Edge detection result saved as edges_output.jpg")

if __name__ == "__main__":
    main()
