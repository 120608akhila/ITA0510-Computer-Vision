import cv2
import numpy as np
image = cv2.imread("cv-4.png")

if image is None:
    print("Error: Image not found.")
    exit()

rows, cols = image.shape[:2]
pts1 = np.float32([
    [50, 50],
    [cols - 50, 50],
    [50, rows - 50],
    [cols - 50, rows - 50]
])
pts2 = np.float32([
    [0, 0],
    [cols - 100, 50],
    [100, rows - 100],
    [cols, rows]
])
M = cv2.getPerspectiveTransform(pts1, pts2)

perspective = cv2.warpPerspective(image, M, (cols, rows))

cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformation", perspective)

cv2.imwrite("perspective_image.jpg", perspective)

print("Perspective transformed image saved successfully!")

cv2.waitKey(0)
cv2.destroyAllWindows()
