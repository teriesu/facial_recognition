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

