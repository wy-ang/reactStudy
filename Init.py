from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('reactStudy')
        self.resize(500, 500)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv);

    window = Window();
    window.setWindowTitle('test')
    window.resize(200,200)
    window.show()

    sys.exit(app.exec_())