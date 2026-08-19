import cv2

# Video path
video_path = r"C:\Users\akhil\Documents\LABS\cv\cv-6.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Video not found!")
else:
    frames = []

    # Read and store all frames
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    cap.release()

    print("Playing video in reverse...")

    # Play frames from last to first
    for frame in reversed(frames):
        cv2.imshow("Reverse Video", frame)

        # Press ESC to stop
        if cv2.waitKey(30) & 0xFF == 27:
            break

    cv2.destroyAllWindows()
