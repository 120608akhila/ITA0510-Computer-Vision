import cv2
import numpy as np

# Read image
img = cv2.imread("cv-5.png")

if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel Gradient Masks
Gx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]], dtype=np.float32)

Gy = np.array([[-1, -2, -1],
               [ 0,  0,  0],
               [ 1,  2,  1]], dtype=np.float32)

# Apply masks
grad_x = cv2.filter2D(gray, cv2.CV_32F, Gx)
grad_y = cv2.filter2D(gray, cv2.CV_32F, Gy)

# Gradient magnitude
gradient = cv2.magnitude(grad_x, grad_y)
gradient = cv2.convertScaleAbs(gradient)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Gradient Sharpened Image", gradient)

# Save output
cv2.imwrite("gradient_output.jpg", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
