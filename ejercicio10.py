#################################
#    ejercicio10.py
#################################
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# inicializamos la camara 
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))
 
#  permitimos que la camara  se inicie
time.sleep(0.1)
 
# capturamos los frames des de la camara 
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grabamos todo en un array numpy
	image = frame.array
	cv2.imshow("Video", image)
	key = cv2.waitKey(1) & 0xFF
	rawCapture.truncate(0)
	if key == ord("q"):
		break
