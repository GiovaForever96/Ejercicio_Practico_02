# Análisis Geodemográfico y Comparación de Riesgo
### Ejercicio Práctico 2

---

## Descripción del Proyecto

Este proyecto es una API REST desarrollada en **Python con FastAPI** que permite:

- Analizar información demográfica de un país
- Comparar el nivel de riesgo entre dos países
- Visualizar un ranking de los 10 países más poblados
- Mostrar información relevante como bandera, mapa, población, región y moneda

La aplicación consume datos en tiempo real desde la API pública:
- [https://restcountries.com](https://restcountries.com)

La aplicación hace uso de Google Cloud:
- Maps Static API (para visualización de mapas)

---

## Objetivo

Aplicar conceptos de:

- Construcción de APIs REST con **FastAPI**
- Consumo de APIs externas
- Procesamiento de datos en backend
- Renderizado dinámico con **Jinja2**
- Diseño básico de interfaz con HTML + CSS
- Estructuración de un pequeño sistema de análisis basado en reglas
- Arquitectura **MVC** con separación de responsabilidades

---

## Tecnologías Utilizadas

| Tecnología | Uso |
|-----------|-----|
| Python 3 | Lenguaje principal |
| **FastAPI** | Framework del API REST |
| **Uvicorn** | Servidor ASGI |
| Jinja2 | Motor de plantillas HTML |
| HTML5 + CSS3 | Interfaz de usuario |
| Bootstrap 5 | Estilos y componentes UI |
| RestCountries API | Datos de países en tiempo real |
| Google Maps Static API | Visualización de mapas |

---

## Estructura del Proyecto

```
Ejercicio_Practico_02/
├── app/
│   ├── controllers/
│   │   ├── analysis_controller.py
│   │   ├── compare_controller.py
│   │   ├── ranking_controller.py
│   │   └── view_controller.py
│   ├── services/
│   │   ├── country_service.py
│   │   └── google_maps_service.py
│   ├── static/
│   │   └── styles.css
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── analysis.html
│   │   ├── compare.html
│   │   └── ranking.html
│   └── utils/
├── main.py
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Funcionalidades

### 1. Análisis de País
Permite ingresar el nombre de un país y obtener:
- Población
- Región
- Moneda
- Bandera
- Mapa (Google Maps)
- Índice de riesgo
- Nivel de riesgo (Bajo, Medio, Alto)

### 2. Comparación de Países
Permite ingresar dos países y muestra:
- Puntaje de riesgo de cada uno
- Nivel de riesgo
- País con menor riesgo

### 3. Ranking de Población
Genera automáticamente el Top 10 países más poblados del mundo mostrando:
- Bandera
- Nombre
- Población
- Índice de riesgo
- Nivel de riesgo

---

## Cómo Ejecutar el Proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/GiovaForever96/Ejercicio_Practico_02.git
cd Ejercicio_Practico_02
```

### 2. Crear entorno virtual (recomendado)
```bash
python -m venv venv
```

### 3. Activar entorno virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Mac / Linux:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Ejecutar la aplicación
```bash
python run.py
```

### 6. Abrir en el navegador

| URL | Descripción |
|-----|-------------|
| `http://127.0.0.1:8000` | Interfaz principal |
| `http://127.0.0.1:8000/docs` | Documentación Swagger UI |
| `http://127.0.0.1:8000/redoc` | Documentación ReDoc |

---

## Modelo de Riesgo

El índice de riesgo es un modelo simplificado basado en:
- Tamaño de población
- Densidad poblacional

### Clasificación

| Puntaje | Nivel |
|---------|-------|
| 0 – 4 | Bajo |
| 5 – 7 | Medio |
| 8+ | Alto |

> Este modelo es demostrativo y puede ampliarse con variables económicas o políticas.

---

## Posibles Mejoras Futuras

- Incorporar PIB y tasa de desempleo
- Implementar base de datos (PostgreSQL / SQLite)
- Agregar gráficos estadísticos con Chart.js
- Implementar autenticación de usuarios con JWT
- Optimizar el modelo de riesgo con ponderaciones
- Agregar pruebas automatizadas con pytest

---

## Autor

Proyecto desarrollado por el **Grupo 7**
Ejercicio Práctico 2 – Desarrollo de APIs con FastAPI
