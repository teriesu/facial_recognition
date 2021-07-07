import cv2
import numpy as np

def orderPoints(points):
    n_points = np.concatenate(points[0], points[1], points[2], points[3]).tolist() #Enlazar matrices
    y_order = sorted(n_points, key = lambda n_points:n_points[1]) #Lambda reconoce como se quiere ordenar
                                                                  #Ordenar hasta la matríz que llega hasta 1
    x1_order = y_order[:2]
    x1_order = sorted(x1_order, key = lambda x1_order:x1_order[0])
    x2_order = y_order[2:4]
    x2_order = sorted(x2_order, key = lambda x2_order:x2_order[0])
    return [x1_order[0], x1_order[1], x2_order[0], x2_order[1]]

#Alineamiento
def alignment(img, width, height):
    imgAligned = None
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    umbralType, umbral = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    cv2.imshow("Umbral", umbral)
    contours, hierarchy  = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0] #El 0 significa que desde el punto 0
                                                                                                   #Lo centre y aplicamos todo
    contours = sorted(contours, key = cv2.contourArea, reverse = True)  #Quiero el ordenado del area de los contornos
                                                                        #Ordena los puntos de mayor a menor
    for c in contours:
        epsilon = 0.01 * cv2.arcLength(c, True) #Dato para encontrar las areas (tiene un valor por defecto)
                                                  #Recorra los puntos de las monedas
        approx = cv2.approxPolyDP(c, epsilon, True) #aproximación al contorno
        if len(approx) == 4:
            puntos = orderPoints(approx) #Envío la aproximación de los 4 puntos
            points1 = np.float32(puntos)
            points2 = np.float32([[0,0], [width, 0], [0, height] , [width, height]])#Existen 4 esquinas y le asignamos coordenadas
            M = cv2.getPerspectiveTransform(points1, points2) #mantener fija la parte de reconocimiento
            imgAligned = cv2.warpPerspective(img, M, (width, height))#Enviar una imágen como "referencia"
    return imgAligned

videoCapture = cv2.VideoCapture(0)

while True:
    typeCamera, frame = captureVideo.read() #La primera variable recibe el timpo de camara
    if typeCamera == False:
        break

    a6img = alignment(frame, width = 677 ,height = 480)

    if a6img is not None:
        points = []
        grayImage = cv2.cvtColor(a6img, cv2.COLOR_RGB2GRAY)
        blur =  cv2.GaussianBlur(grayImage, (5, 5), 1)
        _, umbral = cv2.threshold(blur, 0, 255,cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV)
        cv2.imshow('Umbral', umbral)
        contours, hierarchy  = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(a6img, contours, -1, (0,0,255), 2)
        suma1 = 0.0
        suma2 = 0.0
        for c in contours:
            area = cv2.contourArea(c)
            moments = cv2.moments(c)
            if moments["m00"] == 0:
                moments["m00"] = 1.0
            x = int(moments["m10"]/moments["m00"]) #Momentos en movimiento/ Momentos estáticos
            y = int(moments["m01"]/moments["m00"])

    if cv2.waitKey(1) == ord('q'):
        break
