



# From zero to Facial recognition with OpenCv

## Representación de imágenes

<img src="C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20210610195316461.png" alt="image-20210610195316461" style="zoom:50%;" />

## Escala de grises y Umbralización

<img src="C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20210610195413020.png" alt="image-20210610195413020" style="zoom:50%;" />

Es más sencillo realizar **análisis de imagen**, debido a que los valores no tienen tres valores (R, G, B) sino que de penden únicamente de su brillo. La umbralización hace la diferenciación entre las imágenes claras y oscuras.

### Funciones de opencv

Para realizar el **cambio a escala de grises** se debe emplear la siguiente función:

* cv2.cvtColor(imagen, [Código de colores](https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html))

Para realizar la umbralización se debe emplear la siguiente función:

* cv2.threshold(imagen, límite inferior, límite superior,  [Tipo de Umbralización](https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html)) -> Prueba y error

  * Ejemplo:

    ```python
    ret, thresh1 =  cv2.threshold(img, 127, 255, cv.THRESH_BINARY)
    #Retorna el umbral utilizado y la imágen de umbral
    ```

## Encontrar contornos

Con lo anterior, se puede realizar la segmentación de los contornos de una imagen.

<img src="C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20210610195652267.png" alt="image-20210610195652267" style="zoom:50%;" />

Open cv cuenta con una función para encontrar los contornos de imágenes. Esta se estructura de la siguiente manera:

```python
cv2.findCountours(umbral, mode, method)
```

* El primer parámetro de entrada, es una  imagen umbralizada.

* mode: salida de datos (lista , array, etc... )

* Method:

  * APROX_NONE: 

    <img src="C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20210610201339699.png" alt="image-20210610201339699" style="zoom:33%;" />

  * APROX_SIMPLE:

    <img src="C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20210610201401897.png" alt="image-20210610201401897" style="zoom:33%;" />

### Funciones de opencv

Para realizar el **cambio a escala de grises** se debe emplear la siguiente función:

* cv2.cvtColor(imagen, modo de recuperación del contorno, Tipo de aproximación)

  ```python
  contours, hierarchy =  cv2.findCountours(umbral, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
  #los contornos, la jerarqía
  ```

**EN OPEN CV, EL OBJETO DEBE SER BANCO Y EL FONDO NEGRO**

* cv2.drawContours(img,  contours, contorno que se desea tomar, (R, G, B), Grosor del contorno)

  ```python
  cv2.drawContours(image, contours, 1, (0,255,0), 3)
  #Donde dibujamos el contorno, que contornos pasamos, contorno a dibujar (1,2,3,-1[El -1 selecciona todos], grosor)
  ```

## Filtro Gaussiano (Gauss Blur)

Empleado para el suavizado de imágenes, utilizado cuando hay imágenes borrosas

<img src="https://docs.opencv.org/4.5.2/filter.jpg" alt="filter.jpg" style="zoom:80%;" />

Desaparecen los bordes con pelos de la imágen.

Existen diversos tipos de filtros gaussianos empleados. Se pueden encontrar [aquí](https://docs.opencv.org/4.5.2/d4/d13/tutorial_py_filtering.html)

### Funciones de opencv

Para aplicar el **desenfoque gaussiano** podemos emplear la siguiente función:

```python
desenfoque = cv.GaussianBlur(img, (5,5), 0)
#Imágen a filtrar, (parámetros), 0
```

Como **hallar los parámetros**:

​	Partiendo de que una imagen consiste en una matriz de 3 colores. El gaussian Blur aplica un filtro según la cantidad de pixeles que se asignan en los parámetros. Siendo estos, el tamaño de la caja del filtro a aplicar:

<img src="C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20210618235448231.png" alt="image-20210618235448231" style="zoom:50%;" />

Resultados:

<img src="C:\Users\User\AppData\Roaming\Typora\typora-user-images\image-20210618235545698.png" alt="image-20210618235545698" style="zoom:50%;" />

## Canny

Soluciona los ruidos restantes en la imagen, posterior al filtro gaussiano.

Resalta los bordes de la imágen:

![canny1.jpg](https://docs.opencv.org/3.4/canny1.jpg)

La documentación original de la función la podemos encontrar en el [link](https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html).

### Funciones de opencv

La función que permite aplicar esta función es la siguiente:

```python
border = cv.Canny(img, 100, 200)
#imágen de input, valores variables entre 0 y 255
```

## Morphologyex

Transformaciones morfológicas 

<img src="https://docs.opencv.org/4.5.2/j.png" alt="j.png" style="zoom:50%;" />

1. Erosión

   ```python
   erosion = cv.erode(img,kernel,iterations = 1)
   ```

   <img src="https://docs.opencv.org/4.5.2/erosion.png" alt="erosion.png" style="zoom:50%;" />

2. Dilatación

   ```python
   dilation = cv.dilate(img,kernel,iterations = 1)
   ```

   <img src="https://docs.opencv.org/4.5.2/dilation.png" alt="dilation.png" style="zoom:50%;" />

3. Apertura

   ​	Si hay punticos o pequeño ruido, **fuera** de la imágen principal. Lo elimina

   ```python
   opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
   ```

   <img src="https://docs.opencv.org/4.5.2/opening.png" alt="opening.png" style="zoom:50%;" />

4. Clausura

   ​	Elimina el ruido **dentro** de la imágen principal.

   ```python
   closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
   ```

   <img src="https://docs.opencv.org/4.5.2/closing.png" alt="closing.png" style="zoom:50%;" />

5. Gradiente morfológico

   ```python
   gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
   ```

   <img src="https://docs.opencv.org/4.5.2/gradient.png" alt="gradient.png" style="zoom:50%;" />

6. Top Hat

   ```python
   tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
   ```

   <img src="https://docs.opencv.org/4.5.2/tophat.png" alt="tophat.png" style="zoom:50%;" />

7. Black Hat

   ```python
   blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
   ```

   <img src="https://docs.opencv.org/4.5.2/blackhat.png" alt="blackhat.png" style="zoom:50%;" />

## Contour features

### 2. Area del contorno

```python
area = cv.contourArea(cnt)
```

### 3. Perimetro del contorno

```python
perimeter = cv.arcLength(cnt,True)
#El segundo parametro es True or False dependiendeo si es un contorno cerrado o no (respectivamente)
```

### 4. Aproximación del contorno

En esto, el segundo argumento se llama épsilon, que es la distancia máxima desde el contorno al contorno aproximado. Es un parámetro de precisión. Se necesita una adecuada selección de épsilon para obtener la salida correcta. 

```python
epsilon = 0.1*cv.arcLength(cnt,True)
approx = cv.approxPolyDP(cnt,epsilon,True)
```

En la imagen, la línea verde muestra la curva aproximada para épsilon = 10% de la longitud del arco. La tercera imagen muestra lo mismo para épsilon = 1% de la longitud del arco. 

El tercer argumento especifica si la curva está cerrada o no. 

<img src="https://docs.opencv.org/master/approx.jpg" alt="approx.jpg" style="zoom:67%;" />

### 5. Casco convexo 

```python
hull = cv.convexHull(points[, hull[, clockwise[, returnPoints]]
```

<img src="https://docs.opencv.org/master/convexitydefects.jpg" alt="convexitydefects.jpg" style="zoom:50%;" />

* **Points:** son los contornos por los que pasamos.
* **Hull:** es la salida, normalmente lo evitamos.
* **Clockwise:** bandera de orientación. Si es Verdadero, el casco convexo de salida está orientado en el sentido de las agujas del reloj. De lo contrario, está orientado en sentido antihorario.
* **returnPoints:** Por defecto, True. Luego devuelve las coordenadas de los puntos del casco. Si es falso, devuelve los índices de los puntos de contorno correspondientes a los puntos del casco. 

Entonces, para obtener un casco convexo como en la imagen de arriba, lo siguiente es suficiente: 

```python
hull = cv.convexHull(cnt)
```

### 6. Comprobación de la convexidad 

Existe una función para verificar si una curva es convexa o no, cv.isContourConvex (). Simplemente devuelve si es Verdadero o Falso.

```python
k = cv.isContourConvex(cnt)
```

### 7. Rectángulo delimitador 

#### 	7.a Rectángulo delimitador recto

​			Se encuentra mediante la función cv.boundingRect (). Sea (x, y) la coordenada superior izquierda del rectángulo y (w, h) su ancho y alto. 

```python
x,y,w,h = cv.boundingRect(cnt)
cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)	
```

#### 	7.b Rectángulo girado 

​			Aquí, el rectángulo delimitador se dibuja con un área mínima, por lo que también considera la rotación. La función utilizada es cv.minAreaRect (). 

​			Devuelve una estructura Box2D que contiene los siguientes detalles: (centro (x, y), (ancho, alto), ángulo de rotación). Pero para dibujar este rectángulo, necesitamos 4 esquinas del rectángulo. 

​			Se obtiene mediante la función cv.boxPoints () 

```python
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img,[box],0,(0,0,255),2)
```

<img src="https://docs.opencv.org/master/boundingrect.png" alt="boundingrect.png" style="zoom:50%;" />

### 8. Círculo envolvente mínimo 

Encontramos el círculo circunferencial de un objeto usando la función cv.minEnclosingCircle (). Es un círculo que cubre completamente el objeto con un área mínima. 

```python
(x,y),radius = cv.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv.circle(img,center,radius,(0,255,0),2)
```

<img src="https://docs.opencv.org/master/circumcircle.png" alt="circumcircle.png" style="zoom:50%;" />

### 9. Fitting an Ellipse

El siguiente es ajustar una elipse a un objeto. Devuelve el rectángulo girado en el que está inscrita la elipse. 

```python
ellipse = cv.fitEllipse(cnt)
cv.ellipse(img,ellipse,(0,255,0),2)
```

<img src="https://docs.opencv.org/master/fitellipse.png" alt="fitellipse.png" style="zoom:50%;" />

### 10. Fitting a Line

De manera similar, podemos ajustar una línea a un conjunto de puntos. La imagen de abajo contiene un conjunto de puntos blancos. Podemos aproximarle una línea recta. 

```python
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
```

<img src="https://docs.opencv.org/master/fitline.jpg" alt="fitline.jpg" style="zoom:67%;" />

