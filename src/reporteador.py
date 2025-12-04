import pandas as pd
import os
import matplotlib.pyplot as plt
import textwrap

def generar_reporte_tabular(df_top: pd.DataFrame, metricas: dict, busqueda: str) -> str:
    """
    Genera el reporte final en formato tabular mejorado para la interfaz CLI.
    Limita la longitud de las columnas Nombre y URL para una mejor visualización.
    """
    if df_top.empty:
        return f"\n--- REPORTE OPENPRICE PARA '{busqueda.upper()}' ---\n\n" \
               " No se encontraron productos válidos para generar el reporte."

    reporte = f"\n--- REPORTE OPENPRICE DE COMPARACIÓN ---"
    reporte += f"\nProducto Buscado: {busqueda.upper()}"
    reporte += f"\nTotal de Ítems analizados: {len(df_top)}"
    reporte += "\n" + "=" * 60
    
    reporte += "\n Resumen de Precios (COP):"
    reporte += f"\n   Precio Mínimo: ${metricas.get('Minimo', 0):,}"
    reporte += f"\n   Precio Máximo: ${metricas.get('Maximo', 0):,}"
    reporte += f"\n   Precio Promedio: ${metricas.get('Promedio', 0):,}"
    reporte += "\n" + "=" * 60

    reporte += "\n Detalle del Top 10 (Ordenado por precio ascendente):"
    
    df_tabla = df_top.copy()
    
    df_tabla['Precio (COP)'] = df_tabla['Precio (COP)'].apply(lambda x: f"${x:,.0f}")
    
    df_tabla['Nombre'] = df_tabla['Nombre'].apply(lambda x: textwrap.shorten(x, width=35, placeholder='...'))
    
    df_tabla = df_tabla[['Nombre', 'Precio (COP)', 'URL']]
    
    reporte += "\n" + df_tabla.to_string(index=False)
    reporte += "\n" + "=" * 60
    
    return reporte


def generar_grafico_comparativo(df_top: pd.DataFrame, busqueda: str, ruta_destino: str):
    """
    Genera un gráfico de barras comparando los precios del Top.
    """
    if df_top.empty:
        return False

    precios = df_top['Precio (COP)']
    
    nombres_cortos = [textwrap.shorten(name, width=30, placeholder='...') 
                      for name in df_top['Nombre']]
    
    plt.figure(figsize=(12, 6))
    
    plt.bar(nombres_cortos, precios, color='#FFE600', edgecolor='#333333')
    
    plt.title(f'Comparación de Precios del Top 10: {busqueda.upper()} (COP)', fontsize=14)
    plt.ylabel('Precio (COP)', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10) 
    
    formatter = plt.FuncFormatter(lambda x, p: f'{x:,.0f}')
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    plt.savefig(ruta_destino)
    
    plt.close()
    
    return True