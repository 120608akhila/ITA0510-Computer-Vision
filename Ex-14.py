import cv2
import numpy as np

img = cv2.imread("cv-14.jpeg")

pts1 = np.float32([[50,50],[300,50],[50,300],[300,300]])

pts2 = np.float32([[10,100],[280,50],[80,320],[320,280]])

H, status = cv2.findHomography(pts1, pts2)

output = cv2.warpPerspective(img, H, (img.shape[1], img.shape[0]))

cv2.imshow("Original", img)
cv2.imshow("Homography", output)

cv2.imwrite("homography.jpg", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
