from bs4 import BeautifulSoup
import trained_model_v2
import html2text
import requests
import spacy
import json
import os
import re

#Se define el procesador de lenguaje natural con el modelo de procesamiento de texto trained_model_v2
nlp = spacy.load("trained_model_v2")

#
#Params
##path ubicacion donde se guardara el archivo JSON
##texto que se obtuvo al analizar la informacion con el modelo y que se guarda en el JSON
##ents nombradas del documento que se obtuvieron al analizar el documento
def guardar_json(path,texto,ents):
    entORG = [] #Array de entidades de tipo org
    entLOC = [] #Array de entidades de tipo LOC
    entPER = [] #Array de entidades de tipo PER
    entDATES = [] #Array de entidades de tipo DATES
    entIMPACT = [] #Array de entidades de tipo IMPACT
    entMISC = [] #Array de entidades de tipo MISC
    for ent in ents: #For para guardar las entidades en sus respectivos arrays de almacenamiento
        if ent.label_ == "ORG" :
            entORG.append(ent.text)
        elif ent.label_ == "LOC" :
            entLOC.append(ent.text)
        elif ent.label_ == "PER" :
            entPER.append(ent.text)
        elif ent.label_ == "DATES" :
            entDATES.append(ent.text)
        elif ent.label_ == "IMPACT" :
            entIMPACT.append(ent.text)
        else:
            entMISC.append(ent.text)
    data = {} #Creacion del objeto JSON donde se almacenara la informacion a mostrar en el data.json
    data['text'] = texto #Cargue de informacion en el JSON con su etiqueta
    data['org'] = entORG
    data['loc'] = entLOC
    data['per'] = entPER
    data['dates'] = entDATES
    data['misc'] = entMISC
    data['impact'] = entIMPACT
    dir =   path #Ubicacion donde se debe guardar el documento
    file_name = "data.json" #Nombre con el que se guardara el objecto JSON

    #Metodo para cargar y crear el archivo con el objeto JSON
    with open(os.path.join(dir, file_name), 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)

#### Parametros
##### text: texto a analiazr en formato string ("texto de ejemplo")
##### output_path: ruta absoluta donde se guarga el archivo ("C:\Users\Cat\Documents\")
## El nombre del archivo de salida sera **data.json** y en cada ejecucion se sobreescribira el archivo_
def ner_from_str(text,output_path):    
    doc = nlp(text)
    guardar_json(output_path,text,list(doc.ents))

#### Parametros
##### text_path: ruta del archivo a analizar en formato string ("C:\Users\Cat\Documents\ __archivo.txt__ ")
#El archivo de entrada debe ser un archivo con extension __.txt__*
##### output_path: ruta absoluta donde se guarga el archivo ("C:\Users\Cat\Documents\")
#El nombre del archivo de salida sera **data.json** y en cada ejecucion se sobreescribira el archivo_python
def ner_from_file(text_path, output_path):
    with open(text_path,"r",encoding="utf-8") as f:
        text = f.read().replace("\n", " ").replace("\n\n", " ")
    doc = nlp(text)
    guardar_json(output_path,text,list(doc.ents))

#### Parametros
##### url: ruta del archivo a analizar en formato string ("")
#La url de entrada debe de acceso publico y con contenido en __español__* 
##### output_path: ruta absoluta donde se guarga el archivo ("https://www.web_ejemplo.com/documento")
#El nombre del archivo de salida sera **data.json** y en cada ejecucion se sobreescribira el archivo_python    
def ner_from_url(url, output_path):
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    converter = html2text.HTML2Text()
    plain_text = converter.handle(text)
    clean_text = re.sub(r"\n+", "", plain_text)
    doc = nlp(clean_text)
    guardar_json(output_path,text,list(doc.ents))
