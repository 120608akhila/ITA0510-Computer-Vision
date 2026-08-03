import cv2

# Read image
img = cv2.imread("cv-3.png")

if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel X
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Sobel Y
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Combine X and Y
sobelxy = cv2.addWeighted(cv2.convertScaleAbs(sobelx), 0.5,
                          cv2.convertScaleAbs(sobely), 0.5, 0)

# Display
cv2.imshow("Original Image", img)
cv2.imshow("Sobel XY", sobelxy)

# Save output
cv2.imwrite("sobel_xy.jpg", sobelxy)

cv2.waitKey(0)
cv2.destroyAllWindows()
