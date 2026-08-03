import cv2

# Read image
img = cv2.imread("cv-1.png")

if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel along X-axis
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Convert to absolute values
sobelx = cv2.convertScaleAbs(sobelx)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Sobel X", sobelx)

# Save output
cv2.imwrite("sobel_x.jpg", sobelx)

cv2.waitKey(0)
cv2.destroyAllWindows()
