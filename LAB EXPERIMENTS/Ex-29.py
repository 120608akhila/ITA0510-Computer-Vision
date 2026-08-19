import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-1.png")

if image is None:
    print("Error: Image not found!")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    erosion = cv2.erode(image, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Eroded Image", erosion)

    # Save output
    cv2.imwrite(
        r"C:\Users\akhil\Documents\LABS\cv\erosion_image.jpg",
        erosion
    )

    print("Erosion completed successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
