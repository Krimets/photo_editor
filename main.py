import os

from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog, \
    QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PIL import Image, ImageChops, ImageFont, ImageDraw, ImageFilter

from PIL.ImageFilter import BLUR, DETAIL, SMOOTH, CONTOUR, SHARPEN, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, \
    FIND_EDGES, UnsharpMask, SMOOTH_MORE, GaussianBlur


class ImageEditor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = 'Modified/'

    def load_image(self, filename):
        self.filename = filename
        self.image = Image.open(os.path.join(work_dir, filename))

    def save_image(self):
        path = os.path.join(work_dir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        fullname = os.path.join(path, self.filename)

        self.image.save(fullname)

    def black_white(self):
        self.image = self.image.convert('L')
        self.__save_show_image()

    def __save_show_image(self):
        self.save_image()
        self.show_image(os.path.join(work_dir, self.save_dir, self.filename))

    def turn_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.__save_show_image()

    def turn_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.__save_show_image()

    def flip(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.__save_show_image()

    def blur(self):
        self.image = self.image.filter(BLUR)
        self.__save_show_image()

    def sharpen(self):
        self.image = self.image.filter(SHARPEN)
        self.__save_show_image()

    def contour(self):
        self.image = self.image.filter(CONTOUR)
        self.__save_show_image()

    def detail(self):
        self.image = self.image.filter(DETAIL)
        self.__save_show_image()

    def smooth(self):
        self.image = self.image.filter(SMOOTH)
        self.__save_show_image()

    def smooth_more(self):
        self.image = self.image.filter(SMOOTH_MORE)
        self.__save_show_image()

    def emboss(self):
        self.image = self.image.filter(EMBOSS)
        self.__save_show_image()

    def edge_enhance(self):
        self.image = self.image.filter(EDGE_ENHANCE)
        self.__save_show_image()

    def edge_enhance_more(self):
        self.image = self.image.filter(EDGE_ENHANCE_MORE)
        self.__save_show_image()

    def find_edges(self):
        self.image = self.image.filter(FIND_EDGES)
        self.__save_show_image()

    def unsharp_mask(self):
        self.image = self.image.filter(UnsharpMask)
        self.__save_show_image()

    def gaussian_blur(self):
        self.image = self.image.filter(GaussianBlur)
        self.__save_show_image()

    def show_image(self, path):
        lb_image.hide()
        pixmap_image = QPixmap(path)
        w, h = lb_image.width(), lb_image.height()
        pixmap_image = pixmap_image.scaled(w, h, Qt.AspectRatioMode.KeepAspectRatio)
        lb_image.setPixmap(pixmap_image)
        lb_image.show()


def filter_images(files, extentions):
    return [filename for filename in files for ex in extentions if filename.endswith(ex)]


def choose_work_dir():
    global work_dir
    work_dir = QFileDialog.getExistingDirectory()


def show_filenames_list():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    choose_work_dir()
    filenames = filter_images(os.listdir(work_dir), extensions)

    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)


def show_filename_list():
    extensions = ['.jpeg', '.jpg', '.png', '.bmp', '.gif']
    choose_work_dir()
    filenames = filter_images(os.listdir(work_dir), extensions)

    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)


def info():
    my_info = QMessageBox()
    my_info.setText('Photo Editor\n version 0.94')
    my_info.exec()


def show_choosen_image():
    if lw_files.currentRow() >= 0:
        filename = lw_files.currentItem().text()
        work_image.load_image(filename)
        work_image.show_image(os.path.join(work_dir, work_image.filename))




app = QApplication([])
win = QWidget()
win.resize(1200, 750)
win.setWindowTitle('Photo Editor')

btn_dir = QPushButton('Directory')
lb_image = QLabel('Picture')
lw_files = QListWidget()

btn_left = QPushButton('left')
btn_right = QPushButton('right')
btn_flip = QPushButton('flip')
btn_sharp = QPushButton('sharp')
btn_b_w = QPushButton('black/white')
btn_blur = QPushButton('blur')
btn_contour = QPushButton('contour')
btn_detail = QPushButton('detail')

btn_edge_enhance = QPushButton('edge enhance')
btn_edge_enhance_more = QPushButton('edge enhance more')
btn_emboss = QPushButton('emboss')
btn_find_edges = QPushButton('find edges')
btn_smooth = QPushButton('smooth')
btn_smooth_more = QPushButton('smooth more')
btn_gaussian_blur = QPushButton('gaussian blur')
btn_unsharp_mask = QPushButton('unsharp mask')

btn_info = QPushButton('INFO')

row = QHBoxLayout()
column1 = QVBoxLayout()
column2 = QVBoxLayout()

column1.addWidget(btn_dir)
column1.addWidget(lw_files)
column2.addWidget(lb_image, 95)
column2.addWidget(btn_info)


row_tools1 = QHBoxLayout()
row_tools1.addWidget(btn_left)
row_tools1.addWidget(btn_right)
row_tools1.addWidget(btn_flip)
row_tools1.addWidget(btn_sharp)
row_tools1.addWidget(btn_b_w)
row_tools1.addWidget(btn_blur)
row_tools1.addWidget(btn_contour)
row_tools1.addWidget(btn_detail)

row_tools2 = QHBoxLayout()
row_tools2.addWidget(btn_edge_enhance)
row_tools2.addWidget(btn_edge_enhance_more)
row_tools2.addWidget(btn_emboss)
row_tools2.addWidget(btn_find_edges)
row_tools2.addWidget(btn_smooth)
row_tools2.addWidget(btn_smooth_more)
row_tools2.addWidget(btn_gaussian_blur)
row_tools2.addWidget(btn_unsharp_mask)

column2.addLayout(row_tools1)
column2.addLayout(row_tools2)

row.addLayout(column1, 20)
row.addLayout(column2, 80)

win.setLayout(row)
win.show()

btn_dir.clicked.connect(show_filenames_list)

work_image = ImageEditor()
work_dir = ''

lw_files.currentRowChanged.connect(show_choosen_image)

btn_left.clicked.connect(work_image.turn_left)
btn_right.clicked.connect(work_image.turn_right)
btn_flip.clicked.connect(work_image.flip)
btn_sharp.clicked.connect(work_image.sharpen)
btn_b_w.clicked.connect(work_image.black_white)
btn_blur.clicked.connect(work_image.blur)
btn_contour.clicked.connect(work_image.contour)
btn_detail.clicked.connect(work_image.detail)
btn_edge_enhance.clicked.connect(work_image.edge_enhance)
btn_edge_enhance_more.clicked.connect(work_image.edge_enhance_more)
btn_emboss.clicked.connect(work_image.emboss)
btn_find_edges.clicked.connect(work_image.find_edges)
btn_smooth.clicked.connect(work_image.smooth)
btn_smooth_more.clicked.connect(work_image.smooth_more)
btn_gaussian_blur.clicked.connect(work_image.gaussian_blur)
btn_unsharp_mask.clicked.connect(work_image.unsharp_mask)

btn_info.clicked.connect(info)

app.exec()
