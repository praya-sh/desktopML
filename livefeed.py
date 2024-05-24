import cv2

# Open the video capture device (webcam)
ip = 'http://192.168.0.2:8080/video'
cap = cv2.VideoCapture(ip)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Couldn't open the webcam.")
    exit()

# Infinite loop to continuously read frames from the webcam
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame is read correctly
    if not ret:
        print("Error: Couldn't read frame.")
        break

    # Display the frame in a window named 'Video'
    cv2.imshow('Video', frame)

    # Wait for 1 millisecond and check if 'q' key is pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture device and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
