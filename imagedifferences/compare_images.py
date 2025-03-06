'''
this will not work in codespaces. Try in local box.
'''
import cv2
import numpy as np

def compare_images(image1_path, image2_path):
    """Compares two images and highlights the differences."""

    # Read the images
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # Convert to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference
    diff = cv2.absdiff(gray1, gray2)

    # Threshold the difference image
    _, thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Dilate the threshold image to highlight differences
    kernel = np.ones((5,5), np.uint8)
    dilate = cv2.dilate(thresh, kernel, iterations=2)

    # Find contours in the dilated image
    contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around the differences
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the result
    cv2.imshow("Differences", img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image1_path = "compare_left_image.jpg"
    image2_path = "compare_right_image.jpg"
    compare_images(image1_path, image2_path)

# 512 471 2908  texas univ phone for ms ai
