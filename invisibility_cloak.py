import cv2
import numpy as np
import time

# Initialize webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

time.sleep(2)
for i in range(60):
    ret, background = cap.read()
    background = cv2.flip(background, 1)

print("Background Captured")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    # Flip the frame (optional, makes it mirror-like)
    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([160, 50, 50])
    upper_red1 = np.array([179, 255, 255])
    lower_red2 = np.array([0, 50, 50])
    upper_red2 = np.array([10, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    mask_inv = cv2.bitwise_not(mask)

    res1 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    res2 = cv2.bitwise_and(background, background, mask=mask)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    
    # Display the resulting frame
    cv2.imshow('Invisibility Cloak', final_output)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()
