import cv2
import numpy as np

cap = cv2.VideoCapture("cv-6.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    pts1 = np.float32([[50, 50], [w-50, 50], [50, h-50], [w-50, h-50]])

    pts2 = np.float32([[0, 0], [w, 50], [50, h], [w-50, h-50]])

    M = cv2.getPerspectiveTransform(pts1, pts2)

    output = cv2.warpPerspective(frame, M, (w, h))

    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformation", output)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
