import numpy as np
import cv2

video_file = 'video.mp4'
cap = cv2.VideoCapture(video_file)

while (cap.isOpened()):
    # Captura frame-por-frame
    ret, frame = cap.read()
    if ret == True:
        # trabaja sobre un frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #muestra en pantalla el frame resultante 
        cv2.putText(gray, "Raspberry PI", (10, 25),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow('frame', gray)
        # Exit?
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

