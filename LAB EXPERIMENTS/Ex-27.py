import cv2

# Read source image
source = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-1.png")

# Read destination image
destination = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\cv-2.png")

# Check images
if source is None:
    print("Error: Source image not found!")
elif destination is None:
    print("Error: Destination image not found!")
else:
    # Crop part of source image
    crop = source[50:250, 50:250]

    # Copy cropped image into destination image
    destination[50:250, 50:250] = crop

    # Display results
    cv2.imshow("Source Image", source)
    cv2.imshow("Cropped Image", crop)
    cv2.imshow("Final Image", destination)

    # Save final image
    cv2.imwrite(
        r"C:\Users\akhil\Documents\LABS\cv\cropped_pasted_image.jpg",
        destination
    )

    print("Cropping, copying and pasting completed successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
