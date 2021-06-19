import cv2
image = cv2.imread('contorno.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, umbral = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV) #El subguión ignora la imagen
                                                             #el 100 se escoge a prueba y error
contours, hierarchy  = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0,255,0), 3)
#Mostrar
cv2.imshow('Original image', image)
# cv2.imshow('Gray image', gray)
# cv2.imshow('Umbral image', umbral)
cv2.waitKey(0) #Si se pone 1, se ejecuta mientras la camara, o un video este activado,
               #0 no permite el flijo, por lo que es más util con imagenes
cv2.destroyAllWindows()
