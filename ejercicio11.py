#####################################
#        ejercicio11.py
#####################################
from imutils.video import VideoStream
import numpy as np
import imutils
import time
import cv2

vs = VideoStream(usePiCamera = 1).start()
time.sleep(2.0)
##definimos el codec a usar 
fourcc = cv2.VideoWriter_fourcc(*"XVID")
writer = None
(h, w) = (None, None)
zeros = None

while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=300)
	if writer is None:
		(h, w) = frame.shape[:2]
		writer = cv2.VideoWriter("video.avi", fourcc, 25,(w * 2, h * 2), True)
		zeros = np.zeros((h, w), dtype="uint8")
	(B, G, R) = cv2.split(frame)
	R = cv2.merge([zeros, zeros, R])
	G = cv2.merge([zeros, G, zeros])
	B = cv2.merge([B, zeros, zeros])
	output = np.zeros((h * 2, w * 2, 3), dtype="uint8")
	output[0:h, 0:w] = frame
	output[0:h, w:w * 2] = R
	output[h:h * 2, w:w * 2] = G
	output[h:h * 2, 0:w] = B
	writer.write(output)

	cv2.imshow("Original", frame)
	cv2.imshow("Salida", output)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
cv2.destroyAllWindows()
vs.stop()
writer.release()
