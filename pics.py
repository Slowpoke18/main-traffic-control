import cv2
import numpy as np
import time

# Set the capture interval (in seconds)
capture_interval = 5

# Set the starting index for the image names
start_index = 1

# Set the path where you want to save the frames
save_path = r"C:\Users\abdul\OneDrive\Desktop\camera images\\"

# Create a VideoCapture object to capture frames from the iVCam source
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)  # Use 1 for the second camera (iVCam virtual camera)

# Start an infinite loop for capturing frames
frame_count = start_index  # Initialize the frame count
while True:
    # Read a frame from the video source
    ret, frame = cap.read()

    # Check if the frame is successfully read
    if not ret:
        print("Error reading frame")
        break

    # Get the current timestamp for the frame
    timestamp = int(time.time())

    # Save the frame with a unique filename based on the frame count
    filename = save_path + str(frame_count) + ".jpg"
    cv2.imwrite(filename, frame)

    # Display a message indicating the frame is saved
    print("Frame saved:", filename)

    # Increment the frame count
    frame_count += 1

    # Wait for the specified interval before capturing the next frame
    time.sleep(capture_interval)

# Release the video capture and close any open windows
cap.release()
cv2.destroyAllWindows()
