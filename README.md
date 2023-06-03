# TEAM C3D 
### CODEFEST AD ASTRA 2023

## Identificación de entidades en noticias
Para el cumplimiento de este objetivo se hizo uso de la librería [Spacy](https://spacy.io/) en su última versión, random (de python) adicionalmente se hizo un re-entrenamiento del modelo "es_core_news_lg", la versión más avanzada de detección en **español**, donde se adicionó una capa extra que implementa la detección e indexación de organizaciones (__org__), locaciones (__loc__), personas (__per__), fechas (__dates__), miscelánea (__misc__) e impactos (__impact__).

Los valores que se usaron como datos de entrenamiento fueron seleccionados manualmente buscando la mayor cantidad de variaciones o ejemplares posibles de cada entidad a ser indexados. Además, en cada época, de 100, con uso de la librería random se alimenta el modelo con una entrada aleatoria de los elementos por vez.

Finalmente, se obtuvo un porcentaje de acertación (accuracy) del __82,2%__ con una muestra calificativa de 5 textos nuevos a predecir su respectiva indexación.

Para utilizar este modelo, se debe acceder a la siguiente dirección: [DRIVER](https://drive.google.com/file/d/1-9kE9x8eAf72b3uPzuVObtLSvY90ikky/view?usp=sharing) y descargar el modelo llamado "trained_model_v2".

Después, se debe clonar el repositorio actual donde se encontrará el archivo de funciones para el procesamiento de texto y procesamiento de videos. En el archivo llamado "textAnaly" se encontrarán los métodos para el procesamiento de datos.

Ahora, el archivo comprimido que se descargó del DRIVE debe moverse dentro de la carpeta que se creó al clonar el repositorio y debe quedar como se presenta en la imagen:

![image](https://github.com/Hyosuporte/codefest_c3d/assets/99928498/770428ab-b79a-469d-be02-e097c007a4ef)

Seguido de esto, descomprima la carpeta "trained_model_v2" dentro de la carpeta del repositorio y luego podrá borrar el archivo comprimido como se observa en la imagen:

![image](https://github.com/Hyosuporte/codefest_c3d/assets/99928498/0bbd0b0c-4280-46e5-a143-77c46a8c4cc4)

Después de esto, deberá abrir una terminal de python dentro del proyecto e instalar las siguientes dependencias para poder trabajar:

pip install beautifulsoup4
pip install html2text
pip install requests
pip install spacy

Ahora ya podrá comenzar a usar las funciones de la librería.

Uso del modelo desde texto plano
------
#### Parámetros
##### text: texto a analizar en formato string ("texto de ejemplo")
##### output_path: ruta absoluta donde se guarda el archivo ("C:\Users\Cat\Documents\")
_El nombre del archivo de salida será **data.json** y en cada ejecución se sobreescribirá el archivo_
```python
txtc3d.ner_from_str(text,output_path)
```

Uso del modelo desde texto dentro de un archivo
------
#### Parametros
##### text_path: ruta del archivo a analizar en formato string ("C:\Users\Cat\Documents\ __archivo.txt__ ")
*El archivo de entrada debe ser un archivo con extension __.txt__*
##### output_path: ruta absoluta donde se guarga el archivo ("C:\Users\Cat\Documents\")
_El nombre del archivo de salida sera **data.json** y en cada ejecucion se sobreescribira el archivo_
```python
txtc3d.ner_from_file(text,output_path)
```

Uso del modelo desde texto dentro de un archivo alojado en la nube accedido desde una url __publica__
------

> Para la realización de este metodo de entrada de datos por medio de una url, se implementaron como librerias adiciones (requests, html2test, BeautifulSoup) para extraes el contenido de la pagina en cuestión. Aunque de preferencia se obtendran mejores resultados al pasar contenido con menos ruido.

#### Parametros
##### url: ruta del archivo a analizar en formato string ("")
*La url de entrada debe de acceso publico y con contenido en __español__* 
##### output_path: ruta absoluta donde se guarga el archivo ("https://www.web_ejemplo.com/documento")
_El nombre del archivo de salida sera **data.json** y en cada ejecucion se sobreescribira el archivo_
```python
txtc3d.ner_from_url(url,output_path)
```

## Identificación de entidades en Videos tomados por sensores aéreos
Con el propósito de cumplir con el objetivo propuesto en el CODEFEST respecto a la búsqueda de identificación de entidades en videos usando tecnologías que involucren machine learning, nos proponemos a usar en primera medida la librería [Torch](https://pytorch.org/) en su ultima versión, random (de python) adicionalmente se hizo un re-entrenamiento del modelo "You Only Look Once V5" o conocida por el acrónimo "YOLO5" la cuál es un método de detección de tiempo real, la idea consistía en usar uno de los modelos pre entrenados para tomarlo como punto de partida para volver a someterlo a entrenamiento esta vez usando un dataset dónde sea posible encontrar las entidades objeto de este reto. Para el desarrollo de esta metodología, nos propusimos crear un dataset inicial, este no era nada más  que un video de los entregados(especificamente el video de duración aproximada de 11 minutos), al mismo se le realizaría un proceso de separación de cada uno de sus frames por segundo dando como resultado un total de 790 imagenes diferentes, para la selección de las imagenes que iban a ser usadas para la conformación del dataset decidimos usar un muestreo aleatorio simple en el que a las imagenes se les asigno un número aleatorio entre 0 y 1, se ordeno de mayor a menor y se selecciono un porcentaje mayor al 10% con el objetivo de que esta muestra sea representativa para el universo total. Tras esto se hace una revisión de imagen por imagen para así determinar los distintos objetos geográficos así como algunas geoformas o fenómenos que pueden inferir o ser causados por crimenes como la minería ilegal, la deforestación y la contaminación del Amazonas. Es así que además de las características pedidas por el comite organizador del CODEFEST para el cumplimiento del reto como lo son los vehículos, las construcciones y la deforestación, se adicionan categorías como las de deforestación, erosión, cuerpos de agua y se identifican las coordenadas geográficas del avión al momento de determinar el fenómeno o la entidad de interés.
Para corroborar el seguimiento de la estructura solicitada por YOLO, se implementaron datos de entrenamiento y a su vez datos de validación, el "dataset" construido durante el reto, se adjunó en el repositorio del equipo. 
