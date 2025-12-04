#  OpenPrice: Comparador Ético de Precios (CLI)

##  Resumen del Proyecto

**OpenPrice** es una herramienta desarrollada en **Python**.
Permite **recopilar, analizar y comparar** información de productos de MercadoLibre utilizando técnicas de **Web Scraping responsable**.

El objetivo es ofrecer una solución libre y educativa que automatice la búsqueda y análisis de precios, fomentando el aprendizaje de manipulación de datos y promoviendo el **uso ético y transparente** de la automatización web.

### Funcionalidades Principales (MVP)
* **Adquisición Ética:** Obtención de datos mediante *scraping* con pausas intencionales (`time.sleep`).
* **Análisis:** Cálculo de métricas (Mínimo, Máximo, Promedio) y filtrado del **Top 10** de precios.
* **Reportes:** Generación de un reporte tabular (consola) y un gráfico de barras comparativo (PNG).
* **Interfaces:** Funcionalidad completa desde la **Línea de Comandos (CLI)** y **Web ligera (Flask)** en desarrollo.


##  Licencia

Este proyecto es **Software Libre** y está distribuido bajo la **Licencia Pública General de GNU v3 (GNU GPL v3)**.

Esta licencia asegura que cualquier usuario es libre de usar, estudiar, modificar y compartir el software, garantizando que el código y sus derivados permanezcan libres y abiertos para beneficio de la comunidad.

---

##  Requisitos y Estructura

### Requisitos de Sistema
* **Python:** Versión 3.9 o superior (ej. Python 3.10.12).
* **Sistema Operativo:** Recomendado Linux (GNU/Linux).

### Dependencias de Python
Todas las dependencias:
* `requests`
* `beautifulsoup4`
* `pandas`
* `matplotlib`
* `Flask`

### Instalación de Dependencias

Se recomienda encarecidamente usar un entorno virtual (venv) para aislar las dependencias del sistema:

#### 1. Crear el entorno virtual
python3 -m venv venv

#### 2. Activar el entorno
source venv/bin/activate  # En Linux/macOS
.\venv\Scripts\activate # En Windows PowerShell

#### 3. Instalar dependencias
pip install -r requirements.txt

### Estructura del Proyecto
La aplicación mantiene una estructura modular donde la lógica de negocio se separa de la interfaz de usuario para facilitar el mantenimiento.

```text
OpenPrice/
├── requirements.txt    # Define las dependencias de Python
├── src/                # Contiene toda la lógica de Python y el servidor web
│   ├── app.py          # Aplicación Flask (interfaz web)
│   ├── scraper.py      # Módulo de scraping (extracción de datos)
│   ├── analizador.py   # Módulo de limpieza y cálculo de métricas
│   ├── reporteador.py  # Módulo para generar el gráfico
│   └── main.py         # Punto de entrada para la versión CLI
├── templates/          # Plantillas HTML de Flask (index.html, results.html)
├── static/             # Archivos estáticos: CSS, JS y la imagen de salida (reporte_comparativo.png)
```

##  Uso de la aplicación
OpenPrice puede ejecutarse en dos modos distintos: CLI para la consola, o Web para el navegador.

### 1. Modo Línea de Comandos (CLI)
La versión CLI es ideal para ejecuciones rápidas y automatizadas.

#### Comando de Ejecución:
```text
python src/main.py
```

#### Entrada
Producto a consultar

#### Salida
* El reporte tabular con las métricas y el Top 10 se imprime en la consola.
* Se genera el archivo de imagen reporte_comparativo.png en el directorio raíz del proyecto.

### 2. Modo Web
La versión web ofrece una interfaz gráfica y visualiza los resultados en una página web.

#### Iniciar el servidor:
```text
python src/app.py
```

El servidor se iniciará y mostrará la URL de acceso: http://127.0.0.1:5000.

#### Interacción
1. Abre la URL indicada en tu navegador.
2. Introduce el producto a buscar en el formulario de la página de inicio.
3. Haz clic en "Comparar Precios".

#### Salida:
El navegador muestra la página de resultados con el resumen de métricas, el gráfico comparativo y la tabla detallada del Top 10, todo con un diseño limpio.
