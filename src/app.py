from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import requests
from scraper import obtener_datos, extraer_info
from analizador import limpiar_estructurar, obtener_top, calcular_metricas
from reporteador import generar_grafico_comparativo

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static')
            )

@app.route('/', methods=['GET'])
def index():
    """
    Ruta principal que renderiza el formulario de búsqueda inicial.
    """
    try:
        os.remove(os.path.join(app.root_path, 'static', 'reporte_comparativo.png'))
    except OSError:
        pass

    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """
    Ruta que maneja la búsqueda del producto, ejecuta el scraping y el análisis.
    """
    busqueda = request.form.get('producto')
    
    if not busqueda:
        return redirect(url_for('index'))

    imagen_reporte = 'reporte_comparativo.png'
    ruta_imagen_guardar = os.path.join(app.static_folder, imagen_reporte)

    try:
        print(f"🌐 Ejecutando OpenPrice para: {busqueda}")
        
        html_content = obtener_datos(busqueda) 
        if not html_content:
            return render_template('results.html', busqueda=busqueda, error="No se pudo conectar o la IP fue bloqueada.")

        datos_crudos = extraer_info(html_content)
        df_crudo = pd.DataFrame(datos_crudos)
        
        if df_crudo.empty:
            return render_template('results.html', busqueda=busqueda, error="No se encontraron productos.")

        df_limpio = limpiar_estructurar(df_crudo)
        df_top = obtener_top(df_limpio)
        metricas = calcular_metricas(df_top)

        generar_grafico_comparativo(df_top, busqueda, ruta_imagen_guardar) 
        
        df_html = df_top.to_html(index=False, classes='table table-striped', justify='left')

        return render_template('results.html',
                               busqueda=busqueda,
                               metricas=metricas,
                               df_html=df_html,
                               imagen_reporte=imagen_reporte)
    
    except requests.exceptions.HTTPError as e:
        return render_template('results.html', busqueda=busqueda, error=f"Error HTTP (ej. 404 o 429): {e}")
    except Exception as e:
        print(f" Error en el flujo: {e}")
        return render_template('results.html', busqueda=busqueda, error=f"Ocurrió un error interno: {e}")

if __name__ == '__main__':
    app.run(debug=True)