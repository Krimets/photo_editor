import os
from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, \
    QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from PIL import Image
from PIL.ImageFilter import BLUR, DETAIL


class ImageEditor:
    def __init__(self):
        pass

    def load_image(self, file_name):
        pass

    def save_image(self):
        pass

    def black_white(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def flip(self):
        pass

    def blur(self):
        pass


app = QApplication()
win = QWidget()
win.resize(1200, 750)
win.setWindowTitle('Photo Editor')

app.exec()
