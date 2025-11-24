import pandas as pd
import matplotlib.pyplot as plt
import os

def obtener_top(df_limpio: pd.DataFrame) -> pd.DataFrame:
    """
    Ordena el DataFrame por precio ascendente y obtiene los 10 
    primeros productos para la comparación final.
    """
    if df_limpio.empty:
        print("El DataFrame está vacio, no se puede calcular el Top 10.")
        return pd.DataFrame()
    df_ordenado = df_limpio.sort_values(by='Precio (COP)', ascending=True)
    df_top = df_ordenado.head(10)
    return df_top

def calcular_metricas(df_top: pd.DataFrame) -> dict:
    """
    Calcula el precio minimo, máximo  y promedio del cunjunto de productos del Top.
    Retorna los resultados como un diccionario

    Args:
        df_top (pd.DataFrame): Top de productos
    Returns:
        dict: métricas calculadas
    """
    if df_top.empty:
        return{
            'Minimo': 0,
            'Maximo': 0,
            'Promedio': 0
        }
    columna_precio = 'Precio (COP)'
    precio_min = df_top[columna_precio].min()
    precio_max = df_top[columna_precio].max()
    precio_prom = df_top[columna_precio].mean()
    precio_prom = round(precio_prom)
    metricas = {
        'Minimo': precio_min,
        'Maximo': precio_max,
        'Promedio': precio_prom
    }
    return metricas

def generar_reporte_tabular(df_top: pd.DataFrame, metricas: dict, busqueda: str) -> str:
    """
    Genera el reporte final en formato de cadena de texto (tabular)
    para la interfaz de terminal (CLI).
    """
    if df_top.empty:
        return f"\n--- REPORTE OPENPRICE PARA '{busqueda.upper()}' ---\n\n" \
               " No se encontraron productos válidos para generar el reporte."

    reporte = f"\n--- REPORTE OPENPRICE DE COMPARACIÓN ---"
    reporte += f"\nProducto Buscado: {busqueda.upper()}"
    reporte += f"\nTotal de Ítems analizados: {len(df_top)}"
    reporte += "\n" + "=" * 50
    
    reporte += "\n Resumen de Precios (COP):"
    reporte += f"\n   Precio Mínimo: ${metricas.get('Minimo', 0):,}"
    reporte += f"\n   Precio Máximo: ${metricas.get('Maximo', 0):,}"
    reporte += f"\n   Precio Promedio: ${metricas.get('Promedio', 0):,}"
    reporte += "\n" + "=" * 50

    reporte += "\n Detalle del Top 10 (Ordenado por precio ascendente):"
    
    df_tabla = df_top[['Nombre', 'Precio (COP)', 'URL']].copy()
    
    df_tabla['Precio (COP)'] = df_tabla['Precio (COP)'].apply(lambda x: f"${x:,.0f}")

    reporte += "\n" + df_tabla.to_string(index=False)
    reporte += "\n" + "=" * 50
    
    return reporte



def generar_grafico_comparativo(df_top: pd.DataFrame, busqueda: str):
    """
    Genera un gráfico de barras comparando los precios del Top 10 y lo guarda.
    """
    if df_top.empty:
        print("Advertencia: No hay datos para generar el gráfico.")
        return

    precios = df_top['Precio (COP)']
    
    nombres_cortos = [name[:30] + '...' if len(name) > 30 else name for name in df_top['Nombre']]
    
    plt.figure(figsize=(12, 6))
    
    plt.bar(nombres_cortos, precios, color='#FFE600', edgecolor='#333333')
    
    plt.title(f'Comparación de Precios del Top 10: {busqueda.upper()} (COP)', fontsize=14)
    plt.ylabel('Precio (COP)', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10) 
    
    formatter = plt.FuncFormatter(lambda x, p: f'{x:,.0f}')
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    ruta_imagen = os.path.join(os.getcwd(), 'reporte_comparativo.png')
    plt.savefig(ruta_imagen)