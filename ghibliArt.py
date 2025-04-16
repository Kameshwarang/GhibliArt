import cv2
import numpy as np


def cartoonize_image(image_path, output_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (450, 450))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    edges = cv2.adaptiveThreshold(gray, 155, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10)
    color = cv2.bilateralFilter(img, 9, 100, 600)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    cv2.imwrite(output_path, cartoon)

    cv2.imshow("cartoonize_image", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


cartoonize_image("kiru.jpeg", "cartoonized_output1.jpg")
