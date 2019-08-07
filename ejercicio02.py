#########################################
#    ejercici02.py
#Captura secuencia de imagen desde Python
#########################################

import time
import picamera

camara = picamera.PiCamera()
camara.resolution=(640,480)
time.sleep(2)

for archivo in camara.capture_continuous('img{counter:03d}.jpg'):
    camara.start_preview()
    print("Captura %s" % archivo)
    time.sleep(60)
