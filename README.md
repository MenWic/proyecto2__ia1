# Clasificador de Tumores: Perceptrón desde Cero

Este proyecto consiste en el desarrollo de una **aplicación visual interactiva** que permite **cargar**, **visualizar** y **clasificar** datos del conjunto **Breast Cancer Wisconsin**, utilizando un **perceptrón** implementado desde cero, sin usar librerías de redes neuronales.

---

## 📌 Objetivos

- Desarrollar una interfaz visual para clasificar tumores como **benignos** o **malignos**.
- Implementar y entrenar un **perceptrón simple** sin usar frameworks de deep learning.
- Visualizar el **proceso de entrenamiento**, las **métricas** de rendimiento y la **frontera de decisión**.
- Exportar resultados en **PNG**, **CSV** y **PDF**.

---

## 📂 Estructura del Proyecto

```
proyecto2_ia1/
│
├── documentos/
│   ├── manual_tecnico.md
│   ├── manual_usuario.md
│   └── analisis_resultados.md
│
├── images/
│   └── capturas/  # Capturas referenciadas en el manual de usuario
│
├── exec/
│   └── app.exe  # Ejecutable
│
├── perceptron/
│   └── modelo.py
│
├── ui/
│   └── app.py
│
├── README.md
└── main.py
```

---

## 🚀 Cómo Ejecutar

1. Instalar las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

2. Ejecutar la aplicación:
   ```bash
   python main.py
   ```

---

## 🛠️ Funcionalidades

- **Carga de datos**: Visualización de scatter plots.
- **Configuración de entrenamiento**:
  - Tasa de aprendizaje (%)
  - Número de épocas
  - Porcentaje de datos a usar
- **Entrenamiento del perceptrón**:
  - Visualización de la frontera de decisión.
  - Visualización de métricas: MSE y Accuracy.
- **Exportación**:
  - PNG de las gráficas.
  - CSV de las métricas.
  - PDF resumen del entrenamiento.

---

## 📄 Documentación

- 📘 [Manual Técnico](documentos/manual_tecnico.md)
- 👨‍💻 [Manual de Usuario](documentos/manual_usuario.md)
- 📊 [Explicación Matemática y Análisis de Resultados](documentos/analisis_resultados.md)

---

## 📈 Dataset Utilizado

- **Breast Cancer Wisconsin (Diagnostic)**:
  - Incluye 30 características numéricas de células.
  - Objetivo: Clasificación binaria (**benigno** o **maligno**).

---

## 🧐 Tecnologías y Librerías

- **Python 3**
- **PyQt5** – Interfaz gráfica.
- **Matplotlib** – Visualización de datos.
- **NumPy** – Cálculos matriciales.
- **FPDF** – Generación de reportes en PDF.

---

## 📌 Consideraciones

- El perceptrón está implementado **desde cero**, sin uso de librerías de redes neuronales.
- Se aplican **buenas prácticas** de programación para modularizar y organizar el proyecto.

---

## 📅 Entrega

- **Fecha límite**: Lunes 28 de abril antes de las 14:00 horas.
- Componentes entregables:
  - Código fuente y ejecutable.
  - Manual técnico.
  - Manual de usuario.
  - Explicación matemática y análisis de resultados.

---
