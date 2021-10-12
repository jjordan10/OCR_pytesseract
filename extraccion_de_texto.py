# Importamos la libreria OpenCv
import cv2
import numpy as np
import time

# Importamos Pytesseract
import pytesseract

tic=time.time()
# Abrimos la imagen
im = cv2.imread("x")

# Utilizamos el método "image_to_string"
# Le pasamos como argumento la imagen abierta con Pillow
texto = pytesseract.image_to_string(im)
# Mostramos el resultado
print(texto)
toc=time.time()
print(tic-toc)
#text_file = open("prueba.txt", "w")

#text_file.write(texto)

#text_file.close()