#################################
#  ejercicio09.py
###############################
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# inicializa la camara en  formato RAW
camera = PiCamera()
camera.resolution = (640,480)
rawCapture = PiRGBArray(camera)
 
#  permitimos que la camara cargue
time.sleep(0.1)
 
# tomamos una captura desde la camara 
camera.capture(rawCapture, format="bgr")
image = rawCapture.array
 
# mostramos en pantalla la imagen
cv2.imwrite( "captura.jpg", image );
cv2.imshow("Image", image)
cv2.waitKey(0)
