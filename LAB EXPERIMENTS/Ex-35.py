import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-1.png")

if image is None:
    print("Error: Image not found!")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply Black Hat operation
    black_hat = cv2.morphologyEx(
        image,
        cv2.MORPH_BLACKHAT,
        kernel
    )

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Black Hat Image", black_hat)

    # Save output
    cv2.imwrite(
        r"C:\Users\akhil\Documents\LABS\cv\black_hat_image.jpg",
        black_hat
    )

    print("Black Hat operation completed successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
