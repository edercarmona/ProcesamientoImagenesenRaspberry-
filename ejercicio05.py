######################################
#            ejercicio05.py
#####################################
import imutils
import cv2
 
image = cv2.imread("conejo.jpg")

#obtenemos  valores de la imagen 
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))

#obtenemos un pixel en especifico
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

cv2.imshow("Imagen", image)

#obtener una region de la imagen
roi = image[40:160, 90:160]
cv2.imshow("ROI", roi)

#cambiando el tamaño
resized = cv2.resize(image, (100, 100))
cv2.imshow("Cambio de Tamaño", resized)

#Rotando Imagen
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("OpenCV Rotacion", rotated)

#Rotando Imagen con una simple linea
rotated2 = imutils.rotate_bound(image, 45)
cv2.imshow("Imutils Rotacion", rotated2)

#Dibujando  un rectangulo
output = image.copy()
cv2.rectangle(output, (90, 40), (160, 160), (0, 0, 255), 2)
cv2.imshow("Rectangulo", output)

#Dibujando un circulo
output = image.copy()
cv2.circle(output, (100, 100), 20, (255, 0, 0), -1)
cv2.imshow("Circle", output)

#dibujando una linea
output = image.copy()
cv2.line(output, (10, 10), (200, 200), (0, 0, 255), 5)
cv2.imshow("Linea", output)

#Colocando Texto
output = image.copy()
cv2.putText(output, "Raspberry PI", (10, 25), 
cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)

cv2.waitKey(0)

