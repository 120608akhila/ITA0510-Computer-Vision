import cv2

img = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-1.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)

cv2.imwrite(r"C:\Users\akhil\Documents\LABS\cv\grayscale_image.png", gray)

print("Grayscale image saved successfully!")

cv2.waitKey(0)
cv2.destroyAllWindows()
