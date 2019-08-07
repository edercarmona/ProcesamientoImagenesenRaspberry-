import picamera
import time

for i in range(60):
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        time.sleep(1) # Inicializando Camara
        filename = 'imagen%02d.jpg' % i
        camera.start_preview()
        camera.capture(filename)
        print('Captura %s' % filename)
    time.sleep(59)
