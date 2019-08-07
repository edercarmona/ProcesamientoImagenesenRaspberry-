#################################
#        ejercicio06.py
################################

import imutils
import cv2
 #cargando Imagen
image = cv2.imread("tetris.png")
cv2.imshow("1 Imagen Original", image)
 
#Pasando a Escala de Grises 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("2 Escala de Grises", gray)

#deteccion de  bordes
edged = cv2.Canny(gray, 30, 150)
cv2.imshow("3 Bordes", edged)

#Umbrales
thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("4 Umbrales", thresh)

#thresh1 = cv2.threshold(gray,225,255,cv2.THRESH_BINARY)[1]
#cv2.imshow("5 Umbrales", thresh1)
#thresh2 = cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]
#cv2.imshow("6 Umbrales", thresh2)
#thresh3 = cv2.threshold(gray,225,255,cv2.THRESH_TRUNC)[1]
#cv2.imshow("7 Umbrales", thresh3)
#thresh4 = cv2.threshold(gray,225,255,cv2.THRESH_TOZERO)[1]
#cv2.imshow("8 Umbrales", thresh4)
#thresh5 = cv2.threshold(gray,225,255,cv2.THRESH_TOZERO_INV)[1]
#cv2.imshow("9 Umbrales", thresh5)

#numero  de Objetos
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

#cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#cnts = imutils.grab_contours(cnts)
#output = image.copy()


for c in cnts:
	cv2.drawContours(output, [c], -1, (240, 0, 159), 3)
	cv2.imshow("Contornos", output)
	cv2.waitKey(0)

text = "Encontre {} objetos!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,(240, 0, 159), 2)

cv2.imshow("Contornos", output)
cv2.waitKey(0)
