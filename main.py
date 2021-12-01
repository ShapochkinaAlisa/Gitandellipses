import sys
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.coord = (0, 0)
        self.a = True
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.rewind)

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        self.qp = QPainter()
        # Начинаем процесс рисования
        self.qp.begin(self)
        self.draw(self.qp)
        # Завершаем рисование
        self.qp.end()

    def rewind(self):
        self.a = True
        self.repaint()

    def draw(self, qp):
        try:
            if self.a:
                x = random.randint(5, 500)
                y = random.randint(5, 500)
                qp.setBrush(QColor(255, 0, 0))
                num = random.randint(-100, 100)
                qp.drawEllipse(x, y, num, num)
                self.a = False

        except Exception as a:
            print(a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
