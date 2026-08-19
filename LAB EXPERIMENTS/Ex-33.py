import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-2.png")

if image is None:
    print("Error: Image not found!")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply Morphological Gradient
    gradient = cv2.morphologyEx(
        image,
        cv2.MORPH_GRADIENT,
        kernel
    )

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Morphological Gradient", gradient)

    # Save output
    cv2.imwrite(
        r"C:\Users\akhil\Documents\LABS\cv\morphological_gradient.jpg",
        gradient
    )

    print("Morphological Gradient completed successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
