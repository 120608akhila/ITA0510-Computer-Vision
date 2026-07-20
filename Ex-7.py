import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam.")
    exit()

print("Controls:")
print("N - Normal Speed")
print("S - Slow Motion")
print("F - Fast Motion")
print("Q - Quit")

delay = 30 
while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame.")
        break

    cv2.imshow("Webcam Video Processing", frame)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('n'):
        delay = 30      
        print("Normal Speed")
    elif key == ord('s'):
        delay = 100    
        print("Slow Motion")
    elif key == ord('f'):
        delay = 5      
        print("Fast Motion")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
