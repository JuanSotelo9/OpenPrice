import pandas as pd


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