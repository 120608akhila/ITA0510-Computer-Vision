import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-1.png")

if image is None:
    print("Error: Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Define convolution kernel for boundary detection
    kernel = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ])

    # Apply convolution
    boundary = cv2.filter2D(gray, -1, kernel)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Boundary Image", boundary)

    # Save output
    cv2.imwrite(
        r"C:\Users\akhil\Documents\LABS\cv\boundary_image.jpg",
        boundary
    )

    print("Boundary detection completed successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
