#################################
#        ejercici03.py
#Grabando video desde Python
#################################

import picamera

camara = picamera.PiCamera()
camara.resolution = (640, 480)
camara.start_recording('video.h264')
camara.wait_recording(60)
camara.stop_recording()
