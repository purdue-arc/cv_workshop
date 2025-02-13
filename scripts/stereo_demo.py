import cv2

def main():
    left_camera = cv2.VideoCapture(0)  # Change these indices if using external cameras
    right_camera = cv2.VideoCapture(1)
    
    while True:
        retL, left_frame = left_camera.read()
        retR, right_frame = right_camera.read()
        
        if not retL or not retR:
            break
        
        combined = cv2.hconcat([left_frame, right_frame])
        cv2.imshow('Stereo Camera View', combined)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    left_camera.release()
    right_camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()