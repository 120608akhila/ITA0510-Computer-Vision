import cv2
import numpy as np

# Read the given image
image = cv2.imread(r"C:\Users\akhil\Documents\LABS\cv\watch.png")

if image is None:
    print("Error: Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    gray = cv2.GaussianBlur(gray, (9, 9), 2)

    # Detect circular watch dial
    circles = cv2.HoughCircles(
        gray,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=100,
        param1=100,
        param2=40,
        minRadius=40,
        maxRadius=150
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))

        # Draw detected circle
        for x, y, r in circles[0, :1]:
            cv2.circle(image, (x, y), r, (0, 255, 0), 3)
            cv2.putText(
                image,
                "WATCH DETECTED",
                (x - 100, y - r - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        print("Watch recognized successfully!")
    else:
        print("Watch not detected.")

    # Display result
    cv2.imshow("Watch Recognition", image)

    # Save result
    cv2.imwrite(
        r"C:\Users\akhil\Documents\LABS\cv\watch_recognized.jpg",
        image
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()
