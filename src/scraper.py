import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

SITIO_ID = 'MCO'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8'
}

def obtener_datos(nombre):
    """
    Consultar la pagina web de mercado libre con los items
    que se desea consultar
    """
    busqueda_url = nombre.lower().replace(' ', '-')
    url = f"https://listado.mercadolibre.com.co/{busqueda_url}"
    
    print(f"Intentando acceder a: {url}")
    
    try:
        
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        
        time.sleep(2)
        
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        return None
    
def extraer_info(html_content):
    """
    Extraemos la información de interes del html consultado
    de la pagina web de mercadolibre
    """
    if not html_content:
        return []
    
    soup = BeautifulSoup(html_content, 'html.parser')
    resultados = []
    
    items = soup.find_all('li', class_='ui-search-layout__item')
    
    if not items:
        print("Advertencia: No se encontraron items con el selector actual. El selector debe actualizarse.")
        return []
    
    for item in items:
        
        nombre_tag = item.find('h3', class_='poly-component__title-wrapper')
        nombre = nombre_tag.text.strip() if nombre_tag else 'N/A'
        
        precio_container = item.find('span', class_='andes-money-amount andes-money-amount--cents-superscript')
        precio_texto = '0'
        if precio_container:
            fraccion = precio_container.find('span', class_='andes-money-amount__fraction')
            if fraccion:
                precio_texto = fraccion.text
                
        url_tag = item.find('a', class_='poly-component__title')
        url = url_tag['href'] if url_tag and 'href' in url_tag.attrs else 'N/A'
        
        resultados.append({
            'Nombre': nombre,
            'Precio_Texto_Crudo': precio_texto,
            'URL': url
        })
    
    return resultados
            
def limpiar_estructurar(df_crudo):
    """
    Función para limpiar la información extraida
    """
    if df_crudo.empty:
        print("El DataFrame crudo está vacio. No hay datos para limpiar.")
        return pd.DataFrame()
    
    df_limpio = df_crudo.copy()
    
    df_limpio['Precio_Limpio'] = df_limpio['Precio_Texto_Crudo'].apply(str).str.replace(r'[^\d]', '', regex=True)
    
    df_limpio['Precio_Numerico'] = pd.to_numeric(df_limpio['Precio_Limpio'], errors='coerce')
    
    df_limpio = df_limpio.dropna(subset=['Precio_Numerico'])
    df_limpio = df_limpio[df_limpio['Precio_Numerico'] > 0]
    
    df_final = df_limpio[['Nombre', 'Precio_Numerico', 'URL']].rename(
        columns={'Precio_Numerico': 'Precio (COP)'}
    )
    
    return df_final
    
