# Manual de Usuario - Clasificador de Tumores

## Descripción
Esta aplicación permite visualizar, entrenar y clasificar tumores como benignos o malignos utilizando un perceptrón implementado desde cero. Diseñada para ser intuitiva, permite a los usuarios configurar parámetros de entrenamiento y exportar resultados.

---

## Requisitos
- Python 3.12 o superior.
- Librerías necesarias:
  ```bash
  pip install pyqt5 matplotlib numpy pandas fpdf scikit-learn
  ```

## Inicio de la Aplicación
1. Abrir terminal o consola.
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar:
   ```bash
   python main.py
   ```

---

## Interfaz General
La aplicación cuenta con **3 pestañas**:
1. Visualización
2. Entrenamiento
3. Métricas

---

## 1. Pestaña Visualización

### Objetivo:
Permite seleccionar dos características del dataset y visualizar su distribución.

### Uso:
- **Eje X**: Seleccione la primera característica.
- **Eje Y**: Seleccione la segunda característica.
- **Botón "Visualizar Scatter Plot"**: Genera la gráfica de dispersión.

### Imagen Referencia:
- `images/visualizacion_tab.png`

---

## 2. Pestaña Entrenamiento

### Objetivo:
Entrenar el perceptrón con configuraciones personalizadas.

### Configuraciones:
- **Tasa de Aprendizaje (%):** Entre 1 - 100.
- **Número de Épocas:** Entre 1 - 1000.
- **Porcentaje de Datos a Usar:** Entre 1 - 100.

### Pasos:
1. Ajuste los parámetros.
2. Presione **"Entrenar Perceptrón"**.
3. Visualice la **Frontera de Decisión**.
4. Exporte los resultados:
   - PNG: Frontera.
   - CSV: Métricas.
   - PDF: Reporte completo.

### Imagen Referencia:
- `images/entrenamiento_tab.png`
- `images/frontera_decision.png`

---

## 3. Pestaña Métricas

### Objetivo:
Visualizar el rendimiento del modelo durante el entrenamiento.

### Métricas Disponibles:
- **Error Cuadrático Medio (MSE)** por época.
- **Accuracy** por época.

### Exportar:
- PNG: MSE.
- PNG: Accuracy.

### Imagen Referencia:
- `images/metricas_tab.png`
- `images/mse_grafica.png`
- `images/accuracy_grafica.png`

---

## Exportar Reporte PDF

1. Luego del entrenamiento, presione **"Exportar Reporte PDF"**.
2. Se generará un archivo PDF con:
   - Resumen del entrenamiento.
   - Gráficas: Frontera, MSE y Accuracy.

### Imagen Referencia:
- `images/reporte_pdf.png`

---

## Validaciones
- Solo se permite entrenar si las entradas son válidas.
- No se puede exportar sin datos generados.
- Características X e Y deben ser diferentes.

---

## Contacto
Para dudas o soporte, contactar al desarrollador por email: lamr467@gmail.com.

---
