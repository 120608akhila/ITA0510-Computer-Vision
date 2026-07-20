import cv2

image = cv2.imread("cv-1.png")

if image is None:
    print("Error: Image not found.")
    exit()

cv2.imshow("Original Image", image)

bigger = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
cv2.imshow("Bigger Image", bigger)

smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow("Smaller Image", smaller)

cv2.imwrite("bigger_image.jpg", bigger)
cv2.imwrite("smaller_image.jpg", smaller)

print("Images saved successfully!")

cv2.waitKey(0)
cv2.destroyAllWindows()
