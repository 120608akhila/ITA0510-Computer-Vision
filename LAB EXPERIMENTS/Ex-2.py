import cv2

img = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-2.png")

blur = cv2.GaussianBlur(img, (15, 15), 0)

cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blur)

cv2.imwrite(r"C:\Users\akhil\Documents\LABS\cv\blurred_image.png", blur)

print("Blurred image saved successfully!")

cv2.waitKey(0)
cv2.destroyAllWindows()
