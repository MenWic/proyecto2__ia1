# Manual Técnico del Proyecto

## Descripción General
Este proyecto implementa una aplicación visual interactiva que permite clasificar tumores como benignos o malignos a partir del dataset Breast Cancer Wisconsin, utilizando un perceptrón desarrollado desde cero en Python.

---

## Tecnologías y Dependencias

- **Python 3.12**
- **PyQt5**: Interfaz gráfica.
- **Matplotlib**: Graficación.
- **NumPy**: Cálculos matemáticos.
- **Pandas**: Manipulación de datos.
- **FPDF**: Generación de reportes PDF.
- **Scikit-learn**: Carga del dataset.

### Instalación de Dependencias
```bash
pip install pyqt5 matplotlib numpy pandas fpdf scikit-learn
```

---

## Estructura del Proyecto

```
proyecto2_ia1/
|
├── main.py                  # Archivo principal para iniciar la app
├── ui/
|   ├── app.py             # Código de la interfaz y lógica principal
|
├── perceptron/
|   └── modelo.py         # Implementación del perceptrón
|
├── documentos/              # Documentación del proyecto (manuales, etc.)
├── images/                  # Capturas para el manual de usuario
└── README.md                # Descripción general del proyecto
```

---

## Flujo de Funcionamiento

1. El usuario selecciona dos características del dataset.
2. Se visualiza la distribución mediante un **scatter plot**.
3. El usuario configura: tasa de aprendizaje, número de épocas y porcentaje de datos.
4. Se entrena el perceptrón:
   - Se grafica la frontera de decisión.
   - Se muestran gráficas de error cuadrático medio (MSE) y accuracy.
5. El usuario puede exportar resultados a PNG, CSV y PDF.

---

## Detalle de Archivos

### **main.py**
```python
from ui.app import Visualizador

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Visualizador()
    ventana.show()
    sys.exit(app.exec_())
```

### **ui/app.py**

#### Clases:
- `Visualizador(QWidget)`: Clase principal de la interfaz gráfica.
- `QComboBoxLabel(QWidget)`: Widget personalizado para etiquetas con combobox.

#### Métodos Principales:

- **initUI()**: Inicializa las pestañas y widgets.
- **plot_scatter()**: Muestra el scatter plot según características elegidas.
- **train_perceptron()**: Entrena el perceptrón y genera las gráficas.
- **export_frontier/export_mse/export_acc/export_csv/export_pdf()**: Exportan los resultados.

> **Nota**: Las imágenes para el PDF se generan temporalmente con `tempfile`.

#### Variables Importantes:
- `self.X`, `self.y`: Datos del dataset.
- `self.mse_errors`, `self.accuracies`: Historial de entrenamiento.

---

### **perceptron/modelo.py**

#### Clase: `Perceptron`

```python
class Perceptron:
    def __init__(self, learning_rate, epochs):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = 0
        self.errors = []
        self.accuracies = []

    def activation(self, z):
        return 1 / (1 + np.exp(-z))

    def train(self, X, y):
        # Entrenamiento del perceptrón
        ...

    def evaluate(self, X, y):
        # Cálculo de la accuracy
        ...

    def plot_decision_boundary(self, ax, X):
        # Graficar la frontera de decisión
        ...
```

> **Warning**: Se evita el uso de librerías externas de redes neuronales.

---

## Validaciones Implementadas

- Validación de entradas numéricas.
- Evitar exportar sin haber entrenado.
- Prevención de combinaciones repetidas X/Y.

---

## Estado Actual

- [x] Visualización de datos (Scatter plot) parametrizada.
- [x] Entrenamiento con configuración parametrizada.
- [x] Gráficas dinámicas (frontera, MSE, accuracy).
- [x] Exportación completa.
- [x] Reporte PDF funcional.

---
