import cv2

# Read image
img = cv2.imread("cv-4.png")

if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Canny Edge Detection", edges)

# Save output
cv2.imwrite("canny_output.jpg", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
