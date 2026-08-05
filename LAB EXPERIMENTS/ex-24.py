import cv2
import numpy as np

# Read image
img = cv2.imread("cv-4.png")

if img is None:
    print("Image not found!")
    exit()

# High-Boost factor (A >= 1)
A = 2

# High-Boost mask
kernel = np.array([[ 0, -1,  0],
                   [-1, A+4, -1],
                   [ 0, -1,  0]], dtype=np.float32)

# Apply High-Boost filter
highboost = cv2.filter2D(img, -1, kernel)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("High-Boost Sharpened Image", highboost)

# Save output
cv2.imwrite("highboost_output.jpg", highboost)

cv2.waitKey(0)
cv2.destroyAllWindows()
