import cv2
import numpy as np

img = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-4.png")

kernel = np.ones((5,5), np.uint8)

dilate = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilate)

cv2.imwrite(r"C:\Users\akhil\Documents\LABS\cv\dilated_image_cv-4.png", dilate)

print("Output image saved successfully!")

cv2.waitKey(0)
cv2.destroyAllWindows()
