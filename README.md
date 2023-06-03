# TEAM C3D 
### CODEFEST AD ASTRA 2023

## Identificación de entidades en noticias
Para el cumplimiento de este objetivo se hizo uso de la libreria [Spacy](https://spacy.io/) en su ultima versión, random (de python) adicionalmente se hizo un re-entrenamiento del modelo "es_core_news_lg" la version mas avanzada de detecion en **español** donde se adiciono una capa extra que implementa la deteccion e indexación de organizaciones __org__, locaciones __loc__, personas __per__, fechas __dates__, miscelenaea __misc__ e impactos __impact__.

Los valores que se usaron como daatasat de entrenamiento fueron manualmente seleccionados buscando la mayor cantidad de variaciones o ejemplares posibles de cada entidad que a ser indexados. Ademas en cada epoca, de 100, con uso de la libreria random se alimenta el modelo con una entrada aleatoria de los elementos por vez.

Finalemnente se obtubo un porcentaje de acertacion (accuracy) con una muestra calificativa de 5 textos nuevos a predecir su respectiva indexacion de un __82,2%__ final.

Para utilizar este modelo se debe acceder a la siguiente direccion [modeloTextoC3Dteam](https://test.pypi.org/project/textocodefestc3d/1.0.4/) y ejeutar la siguiente serie de comandos:
```python
pip install -i https://test.pypi.org/simple/ textocodefestc3d==1.0.4
import textocodefestc3d as txtc3d
```
Uso del modelo desde texto plano
------
#### Parametros
##### text: texto a analiazr en formato string ("texto de ejemplo")
##### output_path: ruta absoluta donde se guarga el archivo ("C:\Users\Cat\Documents\")
_El nombre del archivo de salida sera **data.json** y en cada ejecucion se sobreescribira el archivo_
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
