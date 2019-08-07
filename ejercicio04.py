###################################
#        ejercicio04.py
##################################
import cv2

# Carga la imagen 
image_path = 'conejo.jpg'
image = cv2.imread(image_path)

# Guarda una copia como png
image_copy_path = 'conejo-copy.png'
cv2.imwrite(image_copy_path, image)

# carga la copia
image_copy = cv2.imread(image_copy_path)

#muestra imagen en  en Pantalla 
cv2.imshow('Original', image)
cv2.imshow('Copia', image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
