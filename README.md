# DATA_INGENERIA

Este repositorio contiene el código relacionado con el ETL, EDA y una aplicación FastAPI para trabajar con varios datasets.los cuales contienen informacion de la plataforma de video juegos steam

## Estructura del Proyecto

- ETL Carpeta que contiene scripts para el proceso ETL de cada dataset.
- EDA Carpeta que contiene Notebooks para el Análisis Exploratorio de Datos de cada dataset.
- Fastapi Carpeta que contiene el código de la aplicación FastAPI.
- Fastapi\main.py Módulos que manejan los endpoints de la API.

## Configuración y Uso

1. **ETL:**

   - Cada script en `ETL` es independiente y puede ejecutarse individualmente, en los mismos estan los comentarios del codigo que hace en el flujo del programa
     - `ETL\ETL_STEAM_GAMES.ipynb`
     - `ETL\ETL_USERS_ITEMS.ipynb`
     - `ETL\ETL_USERS_REVIEWS.ipynb`

2. **EDA:**

   - Los Notebooks en `eda/` contienen análisis exploratorio de datos para cada dataset, en los mismos estan los comentarios del codigo el el flujo del programa
     - `EDA\EDA_STEAM_GAMES.ipynb`
     - `EDA\EDA_USERS_ITEMS.ipynb`
     - `EDA\EDA_USERS_REVIEWS.ipynb`

3. **FastAPI:**

   - Ejecutar la aplicación FastAPI desde el directorio git bash
     cd /d/Users/Cesar/Desktop/Proyecto_individial_1/Data_ingeneria/Fastapi/fastapi-env/Scripts
     source activate
   - Asegúrate de que el entorno virtual esté activado
     source activate
   - Navega al directorio que contiene tu archivo main.py
     cd /d/Users/Cesar/Desktop/Proyecto_individial_1/Data_ingeneria/Fastapi
   - Ejecuta el servidor FastAPI
     uvicorn main:app --reload

   - Acceder a la documentación de la API en [http://127.0.0.1:8000/docs]

4. **requirements.txt:**

- en esta carpeta encontramos todas las dependencias del proyecto
