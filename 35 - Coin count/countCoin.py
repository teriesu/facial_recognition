import cv2
import numpy as np

valGauss = 3
valKernel = 3
original = cv2.imread('monedas.jpg')
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gaussianBlur = cv2.GaussianBlur(gray, (valGauss, valGauss), 0)
canny = cv2.Canny(gaussianBlur, 60, 100)

#Show results
cv2.imshow('Grays', gray)
cv2.imshow('GaussianBlur', gaussianBlur)
cv2.imshow('Canny', canny)
cv2.waitKey(0)
