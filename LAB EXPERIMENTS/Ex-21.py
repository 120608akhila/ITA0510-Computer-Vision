import cv2
import numpy as np

# Read image
img = cv2.imread("cv-1.png")

if img is None:
    print("Image not found!")
    exit()

# Laplacian mask with diagonal neighbors
kernel = np.array([[1, 1, 1],
                   [1,-8, 1],
                   [1, 1, 1]], dtype=np.float32)

# Apply Laplacian filter
laplacian = cv2.filter2D(img, -1, kernel)

# Sharpen image
sharpened = cv2.subtract(img, laplacian)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

# Save output
cv2.imwrite("sharpened_output.jpg", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
