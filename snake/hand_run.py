import cv2
import numpy as np
import pygame
import sys

from snake_game import SnakeGame, SCREEN_WIDTH, SCREEN_HEIGHT, TILE_SIZE

# MediaPipe import
import mediapipe as mp

FPS = 10  # Controls how fast the snake moves

def main():
    """
    Runs the Snake game controlled by approximate hand centroid in the camera feed, 
    detected via MediaPipe Hands.
    """
    # -------------------------
    # 1. Initialize Pygame
    # -------------------------
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game (Hand Control via MediaPipe)")
    clock = pygame.time.Clock()

    game = SnakeGame()

    # -------------------------
    # 2. Initialize Camera
    # -------------------------
    
    # YOUR CODE HERE: Initialize the camera capture object
    # Hint: Use cv2.VideoCapture(0) to open the default camera
    # Hint: Check if the camera is opened successfully
    

    # -------------------------
    # 3. Initialize MediaPipe Hands
    # -------------------------
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    # Configure Hands:
    # - model_complexity=0: faster but less accurate
    # - max_num_hands=1: only track one hand
    # - min_detection_confidence & min_tracking_confidence can be tuned
    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    print("Press 'ESC' or close the window to quit.")

    running = True
    while running:
        clock.tick(FPS)

        # -------------------------
        # 3A. Handle Pygame events
        # -------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # -------------------------
        # 3B. Process camera feed
        # -------------------------
        
        # YOUR CODE HERE: Read a frame from the camera
        # Hint: Use the capture object from 2 to read a frame
        # Hint: cap.read() returns a tuple (ret, frame)
        # Hint: Check if the frame was read successfully
        ret, frame = 
        

        # Flip for a more natural mirror effect
        frame = cv2.flip(frame, 1)

        # YOUR CODE HERE: Convert the frame to RGB for MediaPipe
        # Hint: Use cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert BGR (OpenCV) to RGB (MediaPipe)
        frame_rgb = 
        
        
        results = hands.process(frame_rgb)

        frame_height, frame_width, _ = frame.shape

        # ------------------------------------------------
        # 3C. If a hand is detected, find its "centroid"
        # ------------------------------------------------
        hand_center_x = None
        hand_center_y = None

        if results.multi_hand_landmarks:
            # We only track 1 hand, so grab the first
            hand_landmarks = results.multi_hand_landmarks[0]

            # Option A: Use a specific landmark (e.g., index=9 = "MIDDLE_FINGER_MCP") as the 'control point'
            # Option B: Average all landmarks to find the "centroid" of the hand
            # Below is Option B for a rough centroid:
            x_sum, y_sum = 0.0, 0.0
            for lm in hand_landmarks.landmark:
                x_sum += lm.x
                y_sum += lm.y
            num_points = len(hand_landmarks.landmark)
            hand_center_x = x_sum / num_points
            hand_center_y = y_sum / num_points

            # Convert from normalized [0,1] coordinates to image coordinates
            hand_center_x = int(hand_center_x * frame_width)
            hand_center_y = int(hand_center_y * frame_height)

            # Draw the hand annotations on the frame for debugging
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Mark the centroid
            
            # YOUR CODE HERE: Draw a circle at the hand centroid
            # Hint: Use cv2.circle(frame, center, radius, color, thickness)
            # Hint: Use (hand_center_x, hand_center_y) as the center
            # Hint: Use 8 for the radius, (0, 255, 0) for green, and -1 for thickness
            
            
        # ------------------------------------------------
        # 3D. Map hand position to snake direction
        # ------------------------------------------------
        if hand_center_x is not None and hand_center_y is not None:
            # We'll split into left, right, up, down using 1/3 increments
            new_direction = game.direction  # default to current direction

            if hand_center_x < frame_width / 3:
                new_direction = (-TILE_SIZE, 0)   # Move left
            elif hand_center_x > 2 * (frame_width / 3):
                new_direction = (TILE_SIZE, 0)    # Move right
            elif hand_center_y < frame_height / 3:
                new_direction = (0, -TILE_SIZE)   # Move up
            elif hand_center_y > 2 * (frame_height / 3):
                new_direction = (0, TILE_SIZE)    # Move down

            # Update snake direction
            game.change_direction(new_direction)

        # ------------------------------------------------
        # 3E. Update Snake Game & check for game over
        # ------------------------------------------------
        game.update()
        if game.game_over:
            running = False

        # ------------------------------------------------
        # 3F. Draw the Snake game using Pygame
        # ------------------------------------------------
        game.draw(screen)
        pygame.display.update()

        # ------------------------------------------------
        # 3G. Display camera feed for debugging
        # ------------------------------------------------
        
        # YOUR CODE HERE: Display the camera feed with annotations
        # Hint: Use cv2.imshow("<some name here>", frame)
        
        # Press 'ESC' to quit from OpenCV window
        if cv2.waitKey(1) & 0xFF == 27:
            running = False

    # -------------------------
    # 4. Cleanup
    # -------------------------
    
    # YOUR CODE HERE: Release the camera and close windows
    # Hint: Release the capture (cap) object and close OpenCV windows
    # Hint: Use cap.release() and cv2.destroyAllWindows()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()






###############################

# Solutions (PLEASE DO NOT COPY-PASTE THIS CODE - IT'S FOR REFERENCE ONLY):

# 2. Initialize Camera
'''
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        pygame.quit()
        sys.exit()
'''

# 3B. Process camera feed
'''
    ret, frame = cap.read()
    if not ret:
        print("Warning: Failed to read frame from camera. Exiting.")
        running = False
        break
'''

# 3B. Convert the frame to RGB for MediaPipe
'''
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
'''

# 3C. Draw a circle at the hand centroid
'''
    cv2.circle(frame, (hand_center_x, hand_center_y), 8, (0, 255, 0), -1)
'''

# 3G. Display the camera feed with annotations
'''
    cv2.imshow("MediaPipe Hands", frame)
'''

# 4. Cleanup
'''
    cap.release()
    cv2.destroyAllWindows()
'''