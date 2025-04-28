import sys
import os
import tempfile
import numpy as np
import pandas as pd
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QComboBox, QLineEdit, QTabWidget, QScrollArea, QMessageBox, QFileDialog, QHBoxLayout
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from sklearn.datasets import load_breast_cancer
from fpdf import FPDF

class Visualizador(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Visualización de Datos - Cáncer de Mama")
        self.setGeometry(100, 100, 800, 600)
        self.showMaximized()

        self.dataset = load_breast_cancer()
        self.X = self.dataset.data
        self.y = self.dataset.target
        self.columns = self.dataset.feature_names

        self.initUI()
        

    def update_y_options(self):
        selected_x = self.combo_x.currentIndex()
        for i in range(self.combo_y.count()):
            self.combo_y.model().item(i).setEnabled(True)
        self.combo_y.model().item(selected_x).setEnabled(False)


    def update_x_options(self):
        selected_y = self.combo_y.currentIndex()
        for i in range(self.combo_x.count()):
            self.combo_x.model().item(i).setEnabled(True)
        self.combo_x.model().item(selected_y).setEnabled(False)


    def initUI(self):
        tabs = QTabWidget()

        # TAB VISUALIZACION
        tab_visual = QWidget()
        tab_layout1 = QVBoxLayout()

        self.combo_x = QComboBox()
        self.combo_x.addItems(self.columns)
        tab_layout1.addWidget(QComboBoxLabel("Eje X:", self.combo_x))

        self.combo_y = QComboBox()
        self.combo_y.addItems(self.columns)
        tab_layout1.addWidget(QComboBoxLabel("Eje Y:", self.combo_y))

        self.combo_x.currentIndexChanged.connect(self.update_y_options)
        self.combo_y.currentIndexChanged.connect(self.update_x_options)

        self.button = QPushButton("Visualizar Scatter Plot")
        self.button.setFixedWidth(150)
        self.button.clicked.connect(self.plot_scatter)
        tab_layout1.addWidget(self.button)

        self.figure = Figure(figsize=(12, 4))
        self.canvas = FigureCanvas(self.figure)

        scroll_visual = QScrollArea()
        scroll_visual.setWidgetResizable(True)
        scroll_visual.setWidget(self.canvas)
        tab_layout1.addWidget(scroll_visual)

        tab_visual.setLayout(tab_layout1)
        tabs.addTab(tab_visual, "Visualización")

        # TAB ENTRENAMIENTO
        tab_train = QWidget()
        tab_layout2 = QVBoxLayout()

        self.learning_rate_input = QLineEdit("10")
        self.learning_rate_input.setFixedWidth(150)
        self.epochs_input = QLineEdit("100")
        self.epochs_input.setFixedWidth(150)
        self.percentage_input = QLineEdit("80")
        self.percentage_input.setFixedWidth(150)

        tab_layout2.addWidget(QComboBoxLabel("Tasa de Aprendizaje (%):", self.learning_rate_input))
        tab_layout2.addWidget(QComboBoxLabel("Número de Épocas:", self.epochs_input))
        tab_layout2.addWidget(QComboBoxLabel("Porcentaje de Datos a Usar:", self.percentage_input))

        self.train_button = QPushButton("Entrenar Perceptrón")
        self.train_button.setFixedWidth(150)
        self.train_button.clicked.connect(self.train_perceptron)
        tab_layout2.addWidget(self.train_button)

        self.train_canvas = FigureCanvas(Figure(figsize=(12, 4)))
        scroll_train = QScrollArea()
        scroll_train.setWidgetResizable(True)
        scroll_train.setWidget(self.train_canvas)
        tab_layout2.addWidget(scroll_train)

        button_layout = QHBoxLayout()
        self.export_frontier_btn = QPushButton("Exportar Frontera PNG")
        self.export_frontier_btn.setFixedWidth(150)
        self.export_frontier_btn.clicked.connect(self.export_frontier)
        self.export_csv_btn = QPushButton("Exportar CSV Métricas")
        self.export_csv_btn.setFixedWidth(150)
        self.export_csv_btn.clicked.connect(self.export_csv)
        self.export_pdf_btn = QPushButton("Exportar Reporte PDF")
        self.export_pdf_btn.setFixedWidth(150)
        self.export_pdf_btn.clicked.connect(self.export_pdf)

        button_layout.addWidget(self.export_frontier_btn)
        button_layout.addWidget(self.export_csv_btn)
        button_layout.addWidget(self.export_pdf_btn)
        tab_layout2.addLayout(button_layout)

        tab_train.setLayout(tab_layout2)
        tabs.addTab(tab_train, "Entrenamiento")

        # TAB METRICAS
        tab_metrics = QWidget()
        tab_layout3 = QVBoxLayout()

        self.error_canvas = FigureCanvas(Figure(figsize=(12, 4)))
        self.error_canvas.setMinimumHeight(400)
        scroll_error = QScrollArea()
        scroll_error.setWidgetResizable(True)
        scroll_error.setWidget(self.error_canvas)
        tab_layout3.addWidget(scroll_error)

        self.acc_canvas = FigureCanvas(Figure(figsize=(12, 4)))
        self.acc_canvas.setMinimumHeight(400)
        scroll_acc = QScrollArea()
        scroll_acc.setWidgetResizable(True)
        scroll_acc.setWidget(self.acc_canvas)
        tab_layout3.addWidget(scroll_acc)

        metric_btn_layout = QHBoxLayout()
        self.export_mse_btn = QPushButton("Exportar MSE PNG")
        self.export_mse_btn.setFixedWidth(150)
        self.export_mse_btn.clicked.connect(self.export_mse)
        self.export_acc_btn = QPushButton("Exportar Accuracy PNG")
        self.export_acc_btn.setFixedWidth(150)
        self.export_acc_btn.clicked.connect(self.export_acc)
        metric_btn_layout.addWidget(self.export_mse_btn)
        metric_btn_layout.addWidget(self.export_acc_btn)
        tab_layout3.addLayout(metric_btn_layout)

        tab_metrics.setLayout(tab_layout3)
        tabs.addTab(tab_metrics, "Métricas")

        final_layout = QVBoxLayout()
        final_layout.addWidget(tabs)
        self.setLayout(final_layout)


    def plot_scatter(self):
        x_index = self.combo_x.currentIndex()
        y_index = self.combo_y.currentIndex()

        x_data = self.X[:, x_index]
        y_data = self.X[:, y_index]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.scatter(x_data, y_data, c=self.y, cmap='bwr', alpha=0.7)
        ax.set_xlabel(f"{self.columns[x_index]}")
        ax.set_ylabel(f"{self.columns[y_index]}")
        ax.set_title(f"Distribución (Scatter plot): {self.columns[x_index]} vs {self.columns[y_index]}")
        self.canvas.draw()


    def train_perceptron(self):
        from perceptron.modelo import Perceptron

        try:
            learning_rate = float(self.learning_rate_input.text())
            epochs = int(self.epochs_input.text())
            percentage = float(self.percentage_input.text())

            if not (1 <= learning_rate <= 100):
                raise ValueError("La tasa de aprendizaje debe ser entre 1 - 100.")
            if not (1 <= epochs <= 1000):
                raise ValueError("El número de épocas debe estar entre 1 - 1000.")
            if not (1 <= percentage <= 100):
                raise ValueError("El porcentaje de datos debe estar entre 1 - 100.")

            learning_rate /= 100
            percentage /= 100

        except ValueError as e:
            QMessageBox.critical(self, "Error de Entrada", str(e))
            return

        x_index = self.combo_x.currentIndex()
        y_index = self.combo_y.currentIndex()

        X = self.X[:, [x_index, y_index]]
        y = self.y

        np.random.seed(42)
        indices = np.random.permutation(len(X))
        train_size = int(len(X) * percentage)
        train_idx = indices[:train_size]

        X_train = X[train_idx]
        y_train = y[train_idx]

        perceptron = Perceptron(learning_rate=learning_rate, epochs=epochs)
        perceptron.train(X_train, y_train)

        self.mse_errors = perceptron.errors
        self.accuracies = perceptron.accuracies

        accuracy = perceptron.evaluate(X_train, y_train)

        # Frontera
        fig = self.train_canvas.figure
        fig.clear()
        ax = fig.add_subplot(111)
        ax.scatter(X[:, 0], X[:, 1], c=self.y, cmap='bwr', alpha=0.7)
        ax.set_xlabel(f"{self.columns[x_index]}")
        ax.set_ylabel(f"{self.columns[y_index]}")
        ax.set_title(f"Frontera de Decisión - Exactitud: {accuracy:.2f}")
        ax.legend(handles=[
            ax.scatter([], [], color='red', label='Maligno'),
            ax.scatter([], [], color='blue', label='Benigno')
        ])
        ax.legend(loc='upper right')
        perceptron.plot_decision_boundary(ax, X)
        self.train_canvas.draw()

        # Error Medio Cuadrático (MSE)
        error_fig = self.error_canvas.figure
        error_fig.clear()
        ax2 = error_fig.add_subplot(111)
        ax2.plot(range(1, len(perceptron.errors) + 1), perceptron.errors, marker='o')
        ax2.set_xlabel('Épocas')
        ax2.set_ylabel('Error Cuadrático Medio (MSE)')
        ax2.set_title('Error Medio Cuadrático (MSE) vs Épocas')
        self.error_canvas.draw()

        # Accuracy (Valores correctos respecto a Muestras utilizadas)
        acc_fig = self.acc_canvas.figure
        acc_fig.clear()
        ax3 = acc_fig.add_subplot(111)
        ax3.plot(range(1, len(perceptron.accuracies) + 1), perceptron.accuracies, marker='o', color='green')
        ax3.set_xlabel('Épocas')
        ax3.set_ylabel('Accuracy')
        ax3.set_title('Accuracy vs Épocas')
        self.acc_canvas.draw()


    def export_frontier(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Guardar Frontera", "", "PNG Files (*.png)")
        if filename:
            self.train_canvas.figure.savefig(filename, bbox_inches='tight')


    def export_mse(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Guardar MSE", "", "PNG Files (*.png)")
        if filename:
            self.error_canvas.figure.savefig(filename, bbox_inches='tight')


    def export_acc(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Guardar Accuracy", "", "PNG Files (*.png)")
        if filename:
            self.acc_canvas.figure.savefig(filename, bbox_inches='tight')


    def export_csv(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Guardar CSV", "", "CSV Files (*.csv)")
        if filename:
            data = pd.DataFrame({
                'Epoca': list(range(1, len(self.mse_errors) + 1)),
                'MSE': self.mse_errors,
                'Accuracy': self.accuracies
            })
            data.to_csv(filename, index=False)
            
            
    def export_pdf(self):
        pdf_path, _ = QFileDialog.getSaveFileName(self, "Guardar Reporte PDF", "", "PDF Files (*.pdf)")

        if pdf_path:
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_frontier, \
                tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_mse, \
                tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_acc:

                self.train_canvas.figure.savefig(tmp_frontier.name, bbox_inches='tight')
                self.error_canvas.figure.savefig(tmp_mse.name, bbox_inches='tight')
                self.acc_canvas.figure.savefig(tmp_acc.name, bbox_inches='tight')

                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.cell(200, 10, txt="Resumen de Entrenamiento", ln=True, align='C')
                pdf.ln(10)
                pdf.cell(200, 10, txt=f"Última Exactitud: {self.accuracies[-1]:.2f}", ln=True)
                pdf.cell(200, 10, txt=f"MSE Final: {self.mse_errors[-1]:.4f}", ln=True)
                pdf.ln(10)
                pdf.cell(200, 10, txt="Gráficas Adjuntas:", ln=True)

                pdf.image(tmp_frontier.name, x=10, y=40, w=180)
                pdf.image(tmp_mse.name, x=10, y=120, w=180)
                pdf.image(tmp_acc.name, x=10, y=200, w=180)

                pdf.output(pdf_path)

            os.unlink(tmp_frontier.name)
            os.unlink(tmp_mse.name)
            os.unlink(tmp_acc.name)


class QComboBoxLabel(QWidget):
    def __init__(self, label_text, widget):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel(label_text)
        layout.addWidget(label)
        layout.addWidget(widget)
        layout.setAlignment(label, Qt.AlignLeft)
        layout.setAlignment(widget, Qt.AlignLeft)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Visualizador()
    ventana.show()
    sys.exit(app.exec_())