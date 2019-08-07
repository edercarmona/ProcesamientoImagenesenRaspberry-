#################################
#    ejercici01.py
#Captura de imagen desde Python
#################################
import picamera
import time
camara = picamera.PiCamera()
camara.resolution=(1027,768)
camara.start_preview()
time.sleep(2)
camara.capture('foto.jpg')
