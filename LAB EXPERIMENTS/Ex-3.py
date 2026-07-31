import cv2

img = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-3.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

cv2.imshow("Original Image", img)
cv2.imshow("Canny Edge Image", edges)

cv2.imwrite(r"C:\Users\akhil\Documents\LABS\cv\canny_image_cv-3.png", edges)

print("Canny edge image saved successfully!")

cv2.waitKey(0)
cv2.destroyAllWindows()
