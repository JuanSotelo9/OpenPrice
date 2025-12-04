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
└── venv/               # Entorno virtual de Python


