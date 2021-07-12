from cv2 import cv2
import numpy as np
def ordenarpuntos(puntos):
    n_puntos=np.concatenate([puntos[0],puntos[1],puntos[2],puntos[3]]).tolist() #Enlazar matrices
    y_order=sorted(n_puntos,key=lambda n_puntos:n_puntos[1])#Lambda reconoce como se quiere ordenar
                                                            #Ordenar hasta la matríz que llega hasta 1
    x1_order=y_order[:2]
    x1_order=sorted(x1_order,key=lambda x1_order:x1_order[0])
    x2_order=y_order[2:4]
    x2_order=sorted(x2_order,key=lambda x2_order:x2_order[0])
    return [x1_order[0],x1_order[1],x2_order[0],x2_order[1]]
def alineamiento(imagen,ancho,alto):
    imagen_alineada=None
    grises=cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    tipoumbral,umbral=cv2.threshold(grises, 150,255, cv2.THRESH_BINARY)
    cv2.imshow("Umbral", umbral)
    contorno=cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]#El 0 significa que desde el punto 0
                                                                                    #Lo centre y aplicamos todo
    contorno=sorted(contorno,key=cv2.contourArea,reverse=True)[:1]#Quiero el ordenado del area de los contornos
                                                                  #Ordena los puntos de mayor a menor
    for c in contorno:
        epsilon=0.01*cv2.arcLength(c, True)#Dato para encontrar las areas (tiene un valor por defecto)
                                           #Recorra los puntos de las monedas
        approximacion=cv2.approxPolyDP(c, epsilon, True)#aproximación al contorno
        if len(approximacion)==4:
            puntos=ordenarpuntos(approximacion)#Envío la aproximación de los 4 puntos
            puntos1=np.float32(puntos)
            puntos2=np.float32([[0,0],[ancho,0],[0,alto],[ancho,alto]])#Existen 4 esquinas y le asignamos coordenadas
            M = cv2.getPerspectiveTransform(puntos1, puntos2)#mantener fija la parte de reconocimiento
            imagen_alineada=cv2.warpPerspective(imagen, M, (ancho,alto))#Enviar una imágen como "referencia"
    return imagen_alineada
capturavideo= cv2.VideoCapture(0)

while True:
    tipocamara,camara=capturavideo.read()
    if tipocamara==False:
        break
    imagen_A6=alineamiento(camara,ancho = 625 ,alto = 480)
    if imagen_A6 is not None:
        puntos=[]
        imagen_gris=cv2.cvtColor(imagen_A6,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(imagen_gris,(5,5),1)
        _,umbral2=cv2.threshold(blur,0,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)
        cv2.imshow("Umbral",umbral2)
        contorno2=cv2.findContours(umbral2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        cv2.drawContours(imagen_A6, contorno2, -1, (255,0,0),2)
        suma1=0.0
        suma2=0.0
        for c_2 in contorno2:
            area=cv2.contourArea(c_2)
            Momentos = cv2.moments(c_2)
            if(Momentos["m00"]==0):
                Momentos["m00"]=1.0
            x=int(Momentos["m10"]/Momentos["m00"])
            y=int(Momentos["m01"]/Momentos["m00"])

            if area > 9700 and area < 11000:
                font = cv2.FONT_HERSHEY_SIMPLEX #Escriba un texto simple
                cv2.putText(a6img, 'COP $/. 50', (x, y), font, 0.75, (176, 58, 158), 2)
                suma1 += 50

            if area > 13500 and area < 15500:
                font = cv2.FONT_HERSHEY_SIMPLEX #Escriba un texto simple
                cv2.putText(a6img, 'COP $/. 100', (x, y), font, 0.75, (176, 58, 158), 2)
                suma1 += 100

        total = suma1 + suma2
        print('suma total = ', total)
        cv2.imshow("Imagen A6", imagen_A6)
        cv2.imshow("camara", camara)
    if cv2.waitKey(1) == ord('s'):
        break
capturavideo.release()
cv2.destroyAllWindows()
