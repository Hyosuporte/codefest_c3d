import os
import re
import json
import requests
from bs4 import BeautifulSoup
import spacy
#import trained_model_v2

#Se define el procesador de lenguaje natural con el modelo de procesamiento de texto trained_model_v2
nlp = spacy.load("trained_model_v2")

def guardar_json(path, texto, ents):
    """
    Guarda la información en formato JSON.

    Parameters:
        path (str): Ruta donde se debe guardar el documento.
        texto (str): Texto que se obtuvo al analizar la información con el modelo y que se guarda en el JSON.
        ents (list): Entidades nombradas del documento que se obtuvieron al analizar el documento.

    Returns:
        None

    """
    entidades = {
        'ORG': [],
        'LOC': [],
        'PER': [],
        'DATES': [],
        'IMPACT': [],
        'MISC': []
    }
    
    for ent in ents:
        if ent.label_ in entidades:
            entidades[ent.label_].append(ent.text)
        else:
            entidades['MISC'].append(ent.text)
    
    data = {
        'text': texto,
        'entities': entidades
    }
    
    file_name = "data.json"  # Nombre con el que se guardará el objeto JSON
    file_path = os.path.join(path, file_name)
    
    with open(file_path, 'w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False)

def ner_from_str(text, output_path):
    """
    Realiza el análisis de entidades nombradas a partir de un texto y guarda los resultados en un archivo JSON.

    Parameters:
        text (str): Texto a analizar en formato string.
        output_path (str): Ruta absoluta donde se guarda el archivo.

    Returns:
        None

    """
    doc = nlp(text)
    guardar_json(output_path, text, list(doc.ents))

def ner_from_file(text_path, output_path):
    """
    Realiza el análisis de entidades nombradas a partir de un archivo de texto y guarda los resultados en un archivo JSON.

    Parameters:
        text_path (str): Ruta del archivo a analizar en formato string. El archivo debe tener extensión .txt.
        output_path (str): Ruta absoluta donde se guarda el archivo.

    Returns:
        None

    """
    with open(text_path, "r", encoding="utf-8") as f:
        text = f.read().replace("\n", " ").replace("\n\n", " ")
    doc = nlp(text)
    guardar_json(output_path, text, list(doc.ents))

def ner_from_url(url, output_path):
    """
    Realiza el análisis de entidades nombradas a partir de una URL y guarda los resultados en un archivo JSON.

    Parameters:
        url (str): Ruta del archivo a analizar en formato string. La URL debe ser de acceso público y contener contenido en español.
        output_path (str): Ruta absoluta donde se guarda el archivo.

    Returns:
        None

    """
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    paragraphs = soup.find_all('p')
    text = ' '.join([p.get_text() for p in paragraphs])
    
    doc = nlp(text)
    guardar_json(output_path, text, list(doc.ents))
