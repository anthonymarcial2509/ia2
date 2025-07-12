# Simulador de Ruleta con IA

Este proyecto simula estrategias de ruleta (Martingala, Fibonacci, Paroli) combinadas con predicción de resultados mediante un modelo de inteligencia artificial.

## Características

 - IA con Random Forest (200 árboles) para predecir resultados con mayor precisión
 - Visualización en tiempo real con Streamlit
 - Análisis de ROI, porcentaje de acierto, rachas y estrategias

## Cómo usar

1. Instala las dependencias:

```bash
pip install -r requirements.txt
```
El archivo `requirements.txt` incluye:

- streamlit
- pandas
- scikit-learn
- matplotlib

2. Ejecuta la app con Streamlit:

```bash
streamlit run main.py
```
En despliegues automatizados el archivo `Procfile` ya incluye ese comando, por
lo que la aplicación se iniciará automáticamente en servicios que lo soporten.

3. Ajusta el capital inicial y número de rondas desde la interfaz.

El panel muestra la evolución del capital por estrategia y una tabla resumen con
ROI y porcentaje de acierto para cada método. Además se presenta una tabla con
las predicciones y resultados de cada ronda.

## Licencia

MIT
