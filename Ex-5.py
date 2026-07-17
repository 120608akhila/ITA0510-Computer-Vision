import cv2
import numpy as np

img = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-5.png")

kernel = np.ones((5,5), np.uint8)

erode = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", erode)

cv2.imwrite(r"C:\Users\akhil\Documents\LABS\cv\eroded_image_cv-5.png", erode)

print("Eroded image saved successfully!")

cv2.waitKey(0)
cv2.destroyAllWindows()
