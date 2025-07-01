import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
import os

# Función para guardar el texto formateado en un archivo .txt
def save_as_text(url, soup):
    filename = f"{url.split('//')[1].replace('/', '_')}.txt"
    
    with open(filename, 'w', encoding='utf-8') as file:
        # Escribimos el título de la página (si lo tiene)
        title = soup.title.string if soup.title else 'Sin título'
        file.write(f"Titulo: {title}\n\n")
        
        # Escribimos el contenido de la página, manteniendo el formato
        for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            # Los encabezados los convertimos en mayúsculas o con asteriscos
            file.write(f"\n{'=' * len(element.text)}\n")
            file.write(f"{element.text.upper()}\n")
            file.write(f"{'=' * len(element.text)}\n\n")
        
        # Párrafos
        for paragraph in soup.find_all('p'):
            file.write(paragraph.get_text(strip=True))
            file.write("\n\n")
        
        # Listas ordenadas
        for ol in soup.find_all('ol'):
            for li in ol.find_all('li'):
                file.write(f"1. {li.get_text(strip=True)}\n")
            file.write("\n")
        
        # Listas desordenadas
        for ul in soup.find_all('ul'):
            for li in ul.find_all('li'):
                file.write(f"- {li.get_text(strip=True)}\n")
            file.write("\n")

# Función para obtener y analizar el contenido de una URL
def scrape_url(url, visited_urls):
    if url in visited_urls:
        return  # Si ya hemos visitado esta URL, no la procesamos de nuevo
    visited_urls.add(url)  # Marcamos la URL como visitada
    
    try:
        # Realizamos la solicitud HTTP a la URL
        response = requests.get(url)
        response.raise_for_status()  # Levanta un error si la solicitud fue fallida
        
        # Analizamos el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Guardar el contenido formateado en archivo .txt
        save_as_text(url, soup)

        print(f"Guardado: {url}")
        print('-' * 80)  # Separador entre las páginas

        # Recursión: seguir enlaces internos
        links = soup.find_all('a', href=True)
        for link in links:
            link_url = link['href']
            
            # Si la URL es relativa, la convertimos en absoluta
            link_url = urljoin(url, link_url)

            # Si la URL es interna y no ha sido visitada, la seguimos
            if link_url.startswith('http') and link_url not in visited_urls:
                scrape_url(link_url, visited_urls)  # Llamada recursiva para seguir el enlace

    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a la URL {url}: {e}")

# Lista de URLs iniciales a scrapear
urls_iniciales = [
    'http://www.facmed.unam.mx/bmd/gi_2k8/prods/D.HTM'
]

# Conjunto para llevar un registro de las URLs visitadas
visited_urls = set()

# Iteramos sobre las URLs iniciales y realizamos el scraping
for url in urls_iniciales:
    scrape_url(url, visited_urls)
    time.sleep(2)  # Pausa de 2 segundos para evitar sobrecargar el servidor
