'''import cv2
import numpy as np
url = "http://10.231.60.153:8080/video"
cp = cv2.VideoCapture(url)
while(True):
    camera, frame = cp.read()
    if frame is not None:
        gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Grayscale Frame", gray1)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
    
cv2.destroyAllWindows()'''


import cv2
import numpy as np

# URL for video stream
url = "http://10.231.60.153:8080/video"
cp = cv2.VideoCapture(url)

# Load the image to insert
image_path = r'C:\Users\smuku\DjangoProject\Y22MLOPS\MyGit\sac.png'  # Replace with the correct path to your image
overlay_img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)  # Load the image with alpha channel if available

# Check if the image was loaded correctly
if overlay_img is None:
    print(f"Error: The image at '{image_path}' could not be loaded. Please check the file path.")
else:
    # Resize the image (optional)
    overlay_img = cv2.resize(overlay_img, (150, 150))  # Resize the image to fit on the frame, adjust as needed

    # Check if the image has an alpha channel (4 channels)
    if overlay_img.shape[2] == 4:
        # Split the image into color and alpha channels
        overlay_img_rgb = overlay_img[:, :, :3]  # RGB image
        overlay_alpha = overlay_img[:, :, 3] / 255.0  # Alpha channel, normalized to [0,1]
    else:
        # No alpha channel, just use the RGB image
        overlay_img_rgb = overlay_img
        overlay_alpha = np.ones((overlay_img.shape[0], overlay_img.shape[1]), dtype=np.float32)  # Fully opaque

    while True:
        camera, frame = cp.read()
        if frame is not None:
            # Get frame dimensions
            frame_h, frame_w = frame.shape[:2]

            # Get overlay image dimensions
            img_h, img_w = overlay_img_rgb.shape[:2]

            # Define the position where the image will be inserted (e.g., top-left corner)
            x_offset, y_offset = 50, 50  # Adjust the offset as needed

            # Ensure the image fits within the frame
            if x_offset + img_w <= frame_w and y_offset + img_h <= frame_h:
                # Region of interest (ROI) in the frame where the image will be placed
                roi = frame[y_offset:y_offset + img_h, x_offset:x_offset + img_w]

                # Blend the overlay image with the ROI in the frame
                for c in range(0, 3):  # Loop over the color channels (B, G, R)
                    roi[:, :, c] = (1.0 - overlay_alpha) * roi[:, :, c] + overlay_alpha * overlay_img_rgb[:, :, c]

                # Place the blended region back into the frame
                frame[y_offset:y_offset + img_h, x_offset:x_offset + img_w] = roi
            
            # Display the frame with the inserted image
            cv2.imshow("Video with Image", frame)

        # Exit when 'q' is pressed
        q = cv2.waitKey(1)
        if q == ord("q"):
            break

# Release resources
cp.release()
cv2.destroyAllWindows()
