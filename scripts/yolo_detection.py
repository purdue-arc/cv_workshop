from ultralytics import YOLO
import cv2

def main():
    model = YOLO('yolov8n.pt')  # Load YOLOv8 model
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        results = model(frame)
        
        for result in results:
            frame = result.plot()
        
        cv2.imshow('YOLOv8 Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()