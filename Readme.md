# 🌎 Análisis Geodemográfico y Comparación de Riesgo  
### Ejercicio Práctico 2

## 📌 Descripción del Proyecto
Este proyecto es una aplicación web desarrollada en **Python con Flask** que permite:

- 📊 Analizar información demográfica de un país  
- ⚖️ Comparar el nivel de riesgo entre dos países  
- 📈 Visualizar un ranking de los 10 países más poblados  
- 🌍 Mostrar información relevante como bandera, mapa, población, región y moneda  

La aplicación consume datos en tiempo real desde la API pública:  
- 🔗 https://restcountries.com  

La aplicación hace uso de Google Cloud:
- 🗺️ Maps Static API (para visualización de mapas)
---

## 🎯 Objetivo
Aplicar conceptos de:

- Consumo de APIs REST  
- Procesamiento de datos en backend  
- Renderizado dinámico con Jinja2  
- Diseño básico de interfaz con HTML + CSS  
- Estructuración de un pequeño sistema de análisis basado en reglas  

---

## 🏗️ Tecnologías Utilizadas
- Python 3  
- Flask  
- Jinja2  
- HTML5  
- CSS3  
- Bootstrap 5  
- API externa: RestCountries  

---

## ⚙️ Funcionalidades

### 1️⃣ Análisis de País
Permite ingresar el nombre de un país y obtener:

- Población  
- Región  
- Moneda  
- Bandera  
- Mapa  
- Índice de riesgo  
- Nivel de riesgo (Bajo, Medio, Alto)  

---

### 2️⃣ Comparación de Países
Permite ingresar dos países y muestra:

- Puntaje de riesgo de cada uno  
- Nivel de riesgo  
- País con menor riesgo  

---

### 3️⃣ Ranking de Población
Genera automáticamente el:

📊 **Top 10 países más poblados del mundo**, mostrando:

- Bandera  
- Nombre  
- Población  
- Índice de riesgo  
- Nivel de riesgo  

---

## 🚀 Cómo Ejecutar el Proyecto

1️⃣ Clonar el repositorio:
```bash
git clone <url-del-repositorio>
```

2️⃣ Crear entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
```

3️⃣ Activar entorno virtual:

**Windows**
```bash
venv\Scripts\activate
```

**Mac / Linux**
```bash
source venv/bin/activate
```

4️⃣ Instalar dependencias:
```bash
pip install -r requirements.txt
```

5️⃣ Ejecutar la aplicación:
```bash
python run.py
```

6️⃣ Abrir en el navegador:
```
http://127.0.0.1:5000
```

---

## 🧠 Modelo de Riesgo
El índice de riesgo es un modelo simplificado basado en:

- Tamaño de población  
- Densidad poblacional  

### Clasificación

| Puntaje | Nivel |
|----------|--------|
| 0 – 4    | Bajo   |
| 5 – 7    | Medio  |
| 8+       | Alto   |

Este modelo es demostrativo y puede ampliarse con variables económicas o políticas.

---

## 📈 Posibles Mejoras Futuras
- Incorporar PIB y tasa de desempleo  
- Implementar base de datos  
- Agregar gráficos estadísticos  
- Implementar autenticación de usuarios  
- Optimizar el modelo de riesgo con ponderaciones  

---

## 👨‍💻 Autor
Proyecto desarrollado por el Grupo 7:

**Ejercicio Práctico 2 – Desarrollo Web con Consumo de API**