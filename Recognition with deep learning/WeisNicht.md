# Reconocimiento Facial

## Explicación XML:

El archivo XML, contiene los contornos de distintos ruidos que generan los diferentes posibles elementos encontrados en el fondo de la imagen de un rostro.

## Clasificador en cascada

El `CascadeClassifier` contiene los contornos del ruido presentado en las caras

Para ser empleado, recibe como argumento la imagen en escala de grises. La función tiene la siguiente estructura:

```python
noise = cv.CascadeClassifier('ruta_del_archivo.xml')
...
_, capture = camera.read()
gray = cv.cvtColor(capture, cv.COLOR_BGR2GRAY)
face = noise.detectMultiScale(gray, 1.5, 3)
#imágen de entrada, reducción de las imágenes(porcentaje[1.5 = 50 %, 1.3 = 30%]), este factor reduce la cantidad de errores (por ej si hay 5 rostros [Se calibra sobre la marcha])
```

<img src="C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20210717123654177.png" alt="image-20210717123654177" style="zoom:30%;" />

Para marcar los puntos y líneas, es necesario realizar el recorrido por todos y cada uno de los mismos. Esto se realiza de la siguiente manera:

```python
for (x, y, e1, e2) in face: #de iz a der, arriba abajo, esquina superior iz, esquina inferior der
    cv.rectangle(capture, (x, y), (x+e1, y+e2), (61,221,66), 4) #Dibujamos un rectangulo sobre el vídeo
    												   #donde lo dibuja, Eje X y Y, concatenamos alturas y anchuras, Color, grosor
```

