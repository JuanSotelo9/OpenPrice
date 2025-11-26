import pandas as pd
import requests
from scraper import obtener_datos, extraer_info
from analizador import limpiar_estructurar, obtener_top, calcular_metricas
from reporteador import generar_reporte_tabular, generar_grafico_comparativo

def ejecutar_openprice_cli():
    """
    Función principal de la aplicación OpenPrice en modo CLI.
    Coordina el flujo completo: Búsqueda -> Limpieza -> Análisis -> Reporte.
    """
    print("\n=======================================================")
    print("         OpenPrice: Comparador de Precios CLI         ")
    print("=======================================================")
    while True:
        busqueda = input("Ingrese el nombre del producto a buscar (ej: iPad Pro): ")
        if busqueda.strip():
            break
        print("Por favor, ingrese un producto válido.")

    print(f"\n Iniciando búsqueda responsable de '{busqueda}'...")

    try:
        html_content = obtener_datos(busqueda)
        if not html_content:
            print(" No se pudo obtener el contenido HTML. Revisa la conexión o el bloqueo IP.")
            return

        datos_crudos = extraer_info(html_content)
        df_crudo = pd.DataFrame(datos_crudos)

        if df_crudo.empty:
            print(f" La extracción no encontró resultados para '{busqueda}'.")
            return

        df_limpio = limpiar_estructurar(df_crudo)

        df_top = obtener_top(df_limpio)
        
        if df_top.empty:
            print(" Después de la limpieza, no quedan productos con precios válidos.")
            return

        metricas = calcular_metricas(df_top)
        
        reporte_tabular = generar_reporte_tabular(df_top, metricas, busqueda)
        print(reporte_tabular)

        generar_grafico_comparativo(df_top, busqueda)
        print("\n Proceso completado. El reporte visual está en 'reporte_comparativo.png'")

    except requests.exceptions.HTTPError as e:
        print(f"\n Error HTTP: {e}. Puede ser un error 404 (página no encontrada) o 429 (Too Many Requests).")
    except Exception as e:
        print(f"\n Ocurrió un error inesperado durante la ejecución: {e}")

if __name__ == "__main__":
    ejecutar_openprice_cli()