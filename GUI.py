import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class demo(QWidget):

    def __init__(self, parent=None):
        super(demo, self).__init__(parent)
        layout = QVBoxLayout()

        self.resize(540, 1080)
        self.setWindowTitle("Test_Demo")

        self.btn = QPushButton()
        self.btn.clicked.connect(self.load_left_image)
        self.btn.setText("Load Left Image")
        layout.addWidget(self.btn)

        self.label = QLabel()
        self.label.setFixedWidth(540)
        self.label.setFixedHeight(360)
        self.content = QTextEdit()
        layout.addWidget(self.label)

        self.btn_2 = QPushButton()
        self.btn_2.clicked.connect(self.load_right_image)
        self.btn_2.setText("Load Right Image")
        layout.addWidget(self.btn_2)

        self.label_2 = QLabel()
        self.label_2.setFixedWidth(540)
        self.label_2.setFixedHeight(360)
        self.content_2 = QTextEdit()
        layout.addWidget(self.label_2)

        self.btn_3 = QPushButton()
        self.btn_3.clicked.connect(self.load_image)
        self.btn_3.setText("Depth Estimation")
        layout.addWidget(self.btn_3)

        self.label_3 = QLabel()
        self.label_3.setFixedWidth(540)
        self.label_3.setFixedHeight(360)
        layout.addWidget(self.label_3)

        self.setLayout(layout)

    def load_left_image(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Load Image', '', 'Image files(*.jpg *.gif *.png)')
        self.label.setPixmap(QPixmap(fname))
        self.label.setScaledContents(True)
        self.content.setText(fname)

    def load_right_image(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Load Image', '', 'Image files(*.jpg *.gif *.png)')
        self.label_2.setPixmap(QPixmap(fname))
        self.label_2.setScaledContents(True)
        self.content_2.setText(fname)

    def load_image(self):
        path = self.content.toPlainText()
        path_2 = self.content_2.toPlainText()
        # print(path)
        # print(path_2)
        fname, _ = QFileDialog.getOpenFileName(self, 'Load Image', '', 'Image files(*.jpg *.gif *.png)')
        self.label_3.setPixmap(QPixmap(fname))
        self.label_3.setScaledContents(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileload = demo()
    fileload.show()
    sys.exit(app.exec_())
