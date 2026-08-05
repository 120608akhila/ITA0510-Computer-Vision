import cv2

# Read image
img = cv2.imread("cv-1.png")

if img is None:
    print("Image not found!")
    exit()

# Add watermark text
cv2.putText(img,
            "OpenCV Lab",      # Watermark text
            (50, 50),          # Position (x, y)
            cv2.FONT_HERSHEY_SIMPLEX,
            1,                 # Font size
            (255, 255, 255),   # White color
            2,                 # Thickness
            cv2.LINE_AA)

# Display image
cv2.imshow("Watermarked Image", img)

# Save output
cv2.imwrite("watermarked_image.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
