import cv2
import numpy as np

valGauss = 3 #Siempre valores impares
valKernel = 3 #Siempre valores impares
original = cv2.imread('monedas.jpg')
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gaussianBlur = cv2.GaussianBlur(gray, (valGauss, valGauss), 0) #Desenfoque gaussiano
canny = cv2.Canny(gaussianBlur, 60, 100) #Filtro Canny
kernel = np.ones((valKernel, valKernel), np.uint8) #Matriz de 3x3 a 8 bytes
morpho = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
contours, hierarchy = cv2.findContours(morpho.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #Encuentra los contornos
print("Münzen gefunden: {}".format(len(contours)))
cv2.drawContours(original, contours, -1, (0,255,0), 3)
#Show results
cv2.imshow('Grays', gray)
cv2.imshow('GaussianBlur', gaussianBlur)
cv2.imshow('Canny', canny)
cv2.imshow('Morpho', morpho)
cv2.imshow('Result', original   )
cv2.waitKey(0)
