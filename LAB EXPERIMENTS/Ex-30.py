import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-5.png")

if image is None:
    print("Error: Image not found!")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilation = cv2.dilate(image, kernel, iterations=1)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Dilated Image", dilation)

    # Save output
    cv2.imwrite(
        r"C:\Users\akhil\Documents\LABS\cv\dilation_image.jpg",
        dilation
    )

    print("Dilation completed successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
