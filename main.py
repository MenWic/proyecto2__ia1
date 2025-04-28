import sys
from PyQt5.QtWidgets import QApplication
from ui.app import Visualizador

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Visualizador()
    ventana.show()
    sys.exit(app.exec_())
