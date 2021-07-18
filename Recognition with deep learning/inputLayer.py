
import cv2 as cv
import os
import imutils

#Creacion de carpetas para las imágenes
model = 'SantiagoBilder'
route1 = 'E:/Estudio/Udemy/Facial recognition/Recognition with deep learning'
routeComplete = route1 + '/' + model
if not os.path.exists(routeComplete): # Verificamos la existencia de la ruta
    os.makedirs(routeComplete) #creamos la ruta donde irán las imáges, en caso de no existir

noise = cv.CascadeClassifier('haarcascade_frontalface_default.xml') #Lee los contornos de ruido
camera = cv.VideoCapture(0)
id = 0
while True:
    response, capture = camera.read()
    if response == False: #Si no detecta la camara, terminar el ciclo
        break
    capture = imutils.resize(capture, width = 640)
    gray = cv.cvtColor(capture, cv.COLOR_BGR2GRAY)  #Cambio a escala de grises
    idCapture = capture.copy() #Capturo cada punto de la imagen (Copio las propiedades)

    face = noise.detectMultiScale(gray, 1.3, 5) #que tanta info de la imagen voy a tomar (ver .md)

    for (x, y, e1, e2) in face: #Recorremos los puntos de las imagenes
        cv.rectangle(capture, (x, y), (x+e1, y+e2), (61,221,66), 4) #Dibujo de rectangulo
        capturedFace = idCapture[y:y+e2, x:x+e1] #Obtengo las coordenadas de la cara (lo de adentro del rectangulo)
        capturedFace = cv.resize(capturedFace, (160, 160), interpolation = cv.INTER_CUBIC) #Tamaño de la imágen re hecha
        cv.imwrite(routeComplete + '/ imagen_{}.jpg'.format(id), capturedFace) #Ruta y que imagen se va a guardar
        id += 1
        if id >= 351:
            break

    cv.imshow('Salida', capture)

    if id >= 351:
        break

camera.release()
cv.destroyAllWindows()
