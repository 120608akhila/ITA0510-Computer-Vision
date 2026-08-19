import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-4.png")

if image is None:
    print("Error: Image not found!")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply Opening
    opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Opening Image", opening)

    # Save output
    cv2.imwrite(
        r"C:\Users\akhil\Documents\LABS\cv\opening_image.jpg",
        opening
    )

    print("Opening operation completed successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
