import cv2

cap = cv2.VideoCapture("C:/Users/akhil/Documents/LABS/cv/cv-6.mp4")

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

print("Press:")
print("N - Normal Speed")
print("S - Slow Motion")
print("F - Fast Motion")
print("Q - Quit")

delay = 30  

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video Processing", frame)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('n'):
        delay = 30     
    elif key == ord('s'):
        delay = 100     
    elif key == ord('f'):
        delay = 5      
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
