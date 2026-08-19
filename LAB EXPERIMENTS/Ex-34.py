import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-1.png")

if image is None:
    print("Error: Image not found!")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply Top Hat operation
    top_hat = cv2.morphologyEx(
        image,
        cv2.MORPH_TOPHAT,
        kernel
    )

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Top Hat Image", top_hat)

    # Save output
    cv2.imwrite(
        r"C:\Users\akhil\Documents\LABS\cv\top_hat_image.jpg",
        top_hat
    )

    print("Top Hat operation completed successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
