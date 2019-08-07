#################################
#       ejercicio08.py
################################
import numpy as np
import cv2

video_file = 'video.mp4'
cap = cv2.VideoCapture(video_file)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        #Calculando Posicion del Texto 
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        position = (50, height - 50)
        # Frames per segundo
        fps = "{0:.2f}".format(cap.get(cv2.CAP_PROP_FPS))
        pos = "{0:.0f}".format(cap.get(cv2.CAP_PROP_POS_MSEC))
        text = "FPS: " + fps + " POS: " + pos
        cv2.putText(frame, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1)
        # Mostrando Video
        cv2.imshow("Video", frame)
        # Salir
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

