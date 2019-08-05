######################################
#            ejercicio05.py
#####################################
import imutils
import cv2
 
image = cv2.imread("conejo.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))
 
cv2.imshow("Image", image)

roi = image[40:160, 90:160]
cv2.imshow("ROI", roi)

resized = cv2.resize(image, (100, 100))
cv2.imshow("Fixed Resizing", resized)

center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotation", rotated)

rotated2 = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Bound Rotation", rotated2)


output = image.copy()
cv2.rectangle(output, (90, 40), (160, 160), (0, 0, 255), 2)
cv2.imshow("Rectangle", output)

output = image.copy()
cv2.circle(output, (100, 100), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)

output = image.copy()
cv2.line(output, (10, 10), (200, 200), (0, 0, 255), 5)
cv2.imshow("Line", output)

output = image.copy()
cv2.putText(output, "Raspberry PI", (10, 25), 
cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)

cv2.waitKey(0)
