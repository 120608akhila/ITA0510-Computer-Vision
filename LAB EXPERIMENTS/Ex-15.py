import cv2
import numpy as np

img = cv2.imread("cv-3.png")

if img is None:
    print("Image not found!")
    exit()

src = np.float32([[50,50],[300,50],[50,300],[300,300]])

dst = np.float32([[20,80],[280,40],[80,320],[320,280]])

H, _ = cv2.findHomography(src, dst)

result = cv2.warpPerspective(img, H, (img.shape[1], img.shape[0]))

cv2.imshow("Original", img)
cv2.imshow("DLT Transformation", result)

cv2.imwrite("dlt_output.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
