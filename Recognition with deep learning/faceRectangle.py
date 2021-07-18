import cv2 as cv
import numpy as np
noise = cv.CascadeClassifier('haarcascade_frontalface_default.xml') #Lee los contornos de ruido
camera = cv.VideoCapture(0)
while True:
    _, capture = camera.read()
    gray = cv.cvtColor(capture, cv.COLOR_BGR2GRAY)  #Cambio a escala de grises
    face = noise.detectMultiScale(gray, 1.3, 5)
    for (x, y, e1, e2) in face: #Recorremos los puntos de las imagenes
        cv.rectangle(capture, (x, y), (x+e1, y+e2), (61,221,66), 4) #Dibujo de rectangulo

    cv.imshow('Salida', capture)

    if cv.waitKey(1) == ord('q'):
        break

camera.release()
cv.destroyAllWindows()
