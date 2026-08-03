import cv2

# Read image
img = cv2.imread("cv-2.png")

if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel along Y-axis
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert to absolute values
sobely = cv2.convertScaleAbs(sobely)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Y", sobely)

# Save output
cv2.imwrite("sobel_y.jpg", sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
