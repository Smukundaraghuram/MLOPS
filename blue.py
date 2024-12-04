import cv2
import numpy as np

# Use the computer's webcam as the video source
cp = cv2.VideoCapture(0)

# Define the range of blue color in HSV
lower_blue = np.array([100, 150, 50])   # Lower bound of blue (Hue, Saturation, Value)
upper_blue = np.array([140, 255, 255])  # Upper bound of blue

while True:
    # Capture each frame from the webcam
    ret, frame = cp.read()
    
    if ret:
        # Convert BGR to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask for blue color
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Bitwise-AND mask and original image to show only the blue parts
        blue_objects = cv2.bitwise_and(frame, frame, mask=mask)

        # Display only the blue-colored objects
        cv2.imshow('Blue Objects Only', blue_objects)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cp.release()
cv2.destroyAllWindows()
