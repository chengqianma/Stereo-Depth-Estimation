'''
Example user interface
'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import generate_disparity_image
import display_depth
import config


class SdenetDemo(QWidget):
    '''Define button function and widgets layout'''
    def __init__(self, parent=None):
        super(SdenetDemo, self).__init__(parent)
        grid = QGridLayout()
        self.setLayout(grid)
        self.max_dis = 0
        self.min_dis = 0
        self.width = 640
        self.height = 194
        self.resize(1280, 388)
        self.setWindowTitle("Demo")

        self.btn = QPushButton()
        self.btn.clicked.connect(self.load_left_image)
        self.btn.setText("Load Left Image")
        grid.addWidget(self.btn, 0, 0)

        self.label = QLabel()
        self.label.setFixedWidth(self.width)
        self.label.setFixedHeight(self.height)
        self.content = QTextEdit()
        grid.addWidget(self.label, 1, 0)

        self.btn_2 = QPushButton()
        self.btn_2.clicked.connect(self.load_right_image)
        self.btn_2.setText("Load Right Image")
        grid.addWidget(self.btn_2, 0, 1)

        self.label_2 = QLabel()
        self.label_2.setFixedWidth(self.width)
        self.label_2.setFixedHeight(self.height)
        self.content_2 = QTextEdit()
        grid.addWidget(self.label_2, 1, 1)

        self.btn_3 = QPushButton()
        self.btn_3.clicked.connect(self.load_image)
        self.btn_3.setText("Depth Estimation")
        self.model = QLineEdit()
        grid.addWidget(self.btn_3, 2, 0)

        self.label_3 = QLabel()
        self.label_3.setFixedWidth(self.width)
        self.label_3.setFixedHeight(self.height)
        self.content_3 = QTextEdit()
        grid.addWidget(self.label_3, 3, 0)

        self.btn_4 = QPushButton()
        self.btn_4.clicked.connect(self.load_depth)
        self.btn_4.setText("Display Depth")
        grid.addWidget(self.btn_4, 2, 1)

        self.label_4 = QLabel()
        self.label_4.setFixedWidth(self.width)
        self.label_4.setFixedHeight(self.height)
        grid.addWidget(self.label_4, 3, 1)

    def load_left_image(self):
        '''Load image captured by left lens'''
        fname, _ = QFileDialog.getOpenFileName(self, 'Load Image',
                                               '', 'Image files(*.jpg *.gif *.png)')
        self.label.setPixmap(QPixmap(fname))
        self.label.setScaledContents(True)
        self.content.setText(fname)

    def load_right_image(self):
        '''Load image captured by right lens'''
        fname, _ = QFileDialog.getOpenFileName(self, 'Load Image',
                                               '', 'Image files(*.jpg *.gif *.png)')
        self.label_2.setPixmap(QPixmap(fname))
        self.label_2.setScaledContents(True)
        self.content_2.setText(fname)

    def load_image(self):
        '''Compute the disparity image and show'''
        path = self.content.toPlainText()
        path_2 = self.content_2.toPlainText()
        generate_disparity_image.generate_disparity_image(path, path_2)
        fname = path.split(".")[0] + "_disparity.png"
        self.content_3.setText(fname)
        self.label_3.setPixmap(QPixmap(fname))
        self.label_3.setScaledContents(True)

    def load_depth(self):
        '''Input depth and show the specific depth area'''
        path_3 = self.content_3.toPlainText()
        self.max_dis, self.min_dis = display_depth.max_min_depth(path_3,
                                                                 config.BASELINE,
                                                                 config.FOCAL, config.PIXEL_SIZE)
        num, ok_or_not = QInputDialog.getInt(self, "Demo",
                                             "Depth Min: " + str(self.min_dis) +
                                             " Depth Max: " + str(self.max_dis))

        if ok_or_not:
            display_depth.display_depth(path_3, num)
            fname = "depth_temp.png"
            self.label_4.setPixmap(QPixmap(fname))
            self.label_4.setScaledContents(True)


if __name__ == '__main__':
    APP = QApplication(sys.argv)
    FILELOAD = SdenetDemo()
    FILELOAD.show()
    sys.exit(APP.exec_())
