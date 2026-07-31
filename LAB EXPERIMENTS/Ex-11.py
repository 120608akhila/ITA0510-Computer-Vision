import cv2
import numpy as np


image = cv2.imread("cv-3.png")

if image is None:
    print("Error: Image not found.")
    exit()

rows, cols = image.shape[:2]

pts1 = np.float32([[50, 50],
                   [200, 50],
                   [50, 200]])

pts2 = np.float32([[10, 100],
                   [200, 50],
                   [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)

affine = cv2.warpAffine(image, M, (cols, rows))

cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformation", affine)
cv2.imwrite("affine_image.jpg", affine)

print("Affine transformed image saved successfully!")

cv2.waitKey(0)
cv2.destroyAllWindows()
