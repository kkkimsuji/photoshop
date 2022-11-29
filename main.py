import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtGui import QAction, QImage, QPixmap, QFont, Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow, 
    QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog, QGridLayout 
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Photoshop")

        # 메뉴바 만들기
        self.menu = self.menuBar()
        self.menu.setNativeMenuBar(False)

        #파일 메뉴
        self.new_action = QAction("새로 만들기")
        self.new_action.setShortcut("Ctrl+N")
        self.open = QAction("열기")
        self.open.setShortcut("Ctrl+O")
        self.recent = QAction("최근 소식")
        self.save = QAction("저장")
        self.save.setShortcut("Ctrl+S")
        self.save_othername = QAction("다른 이름으로 저장")
        self.print = QAction("인쇄")
        self.send = QAction("보내기")
        self.image_attribute = QAction("이미지 속성")
        self.image_attribute.setShortcut("Ctrl+E")
        self.setting = QAction("설정")
        self.quit_action = QAction("나가기")
        self.quit_action.triggered.connect(self.close)

        file_menu = self.menu.addMenu("파일")
        file_menu.addAction(self.new_action)
        file_menu.addAction(self.open)
        file_menu.addAction(self.recent)
        file_menu.addAction(self.save)
        file_menu.addAction(self.save_othername)
        file_menu.addSeparator()
        file_menu.addAction(self.print)
        file_menu.addAction(self.send)
        file_menu.addSeparator()
        file_menu.addAction(self.image_attribute)
        file_menu.addSeparator()
        file_menu.addAction(self.setting)
        file_menu.addSeparator()
        file_menu.addAction(self.quit_action)


        # 보기 메뉴
        self.hundred = QAction("100%")
        self.graduated_ruler = QAction("눈금자")
        self.graduated_ruler.setShortcut("Ctrl+R")
        self.grid = QAction("격자")
        self.grid.setShortcut("Ctrl+G")
        self.state = QAction("상태표시줄")
        self.full_screen = QAction("전체화면")
       
        look_menu = self.menu.addMenu("보기")
        look_menu.addAction(self.hundred)
        look_menu.addSeparator()
        look_menu.addAction(self.graduated_ruler)
        look_menu.addAction(self.grid)
        look_menu.addAction(self.state)
        look_menu.addSeparator()
        look_menu.addAction(self.full_screen)
       

        # 제출자 메뉴
        self.it = QAction("IT융합공학과")
        self.num = QAction("2020101462")
        self.name = QAction("김수지")

        me_menu = self.menu.addMenu("제출자")
        me_menu.addAction(self.it)
        me_menu.addAction(self.num)
        me_menu.addAction(self.name)

#################################################################################################################

        # 메인화면 레이아웃
        main_layout = QHBoxLayout()

        # 사이드바 메뉴버튼
        sidebar = QGridLayout()
        button0 = QPushButton("이미지 열기")
        button1 = QPushButton("좌우반전")
        button2 = QPushButton("상하반전")
        button3 = QPushButton("상하좌우반전")
        button4 = QPushButton("흑백변환")
        button5 = QPushButton("확대")
        button6 = QPushButton("축소")
        button7 = QPushButton("45도 회전")
        button8 = QPushButton("90도 회전")
        button9 = QPushButton("축소 회전")
        button10 = QPushButton("어핀변환")
        button11 = QPushButton("원근변환")
        button12 = QPushButton("비선형변환")
        button13 = QPushButton("오목왜곡")
        button14 = QPushButton("볼록왜곡")
        button15 = QPushButton("핀쿠션왜곡")
        button16 = QPushButton("배럴왜곡")
        button17 = QPushButton("좌우거울왜곡")
        button18 = QPushButton("상하거울왜곡")
        button19 = QPushButton("평균블러링")
        button20 = QPushButton("가우시안")
        button21 = QPushButton("미디언")
        button22 = QPushButton("바이레터럴")
        button23 = QPushButton("기본미분")
        button24 = QPushButton("로버츠교차")
        button25 = QPushButton("캐니엣지")
        button26 = QPushButton("프리윗")
        button27 = QPushButton("소벨")
        button28 = QPushButton("라플라시안")
        button29 = QPushButton("컨투어")
        button31 = QPushButton("허프선변환")
        button30 = QPushButton("새로고침")
        button32 = QPushButton("얼굴인식")
        button33 = QPushButton("얼굴자르기")
        button34 = QPushButton("모자이크")
        button35 = QPushButton("블러모자이크") 

        button0.clicked.connect(self.show_file_dialog)
        button1.clicked.connect(self.flip_LR_image)
        button2.clicked.connect(self.flip_updown_image)
        button3.clicked.connect(self.flip_updown_LR_image)  
        button4.clicked.connect(self.color_gray)
        button5.clicked.connect(self.big)
        button6.clicked.connect(self.small)
        button7.clicked.connect(self.rotation_45)
        button8.clicked.connect(self.rotation_90)
        button9.clicked.connect(self.rotation_small)
        button10.clicked.connect(self.affine)
        button11.clicked.connect(self.perspective)
        button12.clicked.connect(self.wave)
        button13.clicked.connect(self.distortion_concave)
        button14.clicked.connect(self.distortion_convex)
        button15.clicked.connect(self.pincushion)
        button16.clicked.connect(self.barrel)
        button17.clicked.connect(self.mirror_LR)
        button18.clicked.connect(self.mirror_UD)
        button19.clicked.connect(self.blur)
        button20.clicked.connect(self.gaussian)
        button21.clicked.connect(self.median)
        button22.clicked.connect(self.bilateral)
        button23.clicked.connect(self.differential)
        button24.clicked.connect(self.roberts)
        button25.clicked.connect(self.canny)
        button26.clicked.connect(self.prewitt)
        button27.clicked.connect(self.sobel)
        button28.clicked.connect(self.laplacian)
        button29.clicked.connect(self.contour)
        button31.clicked.connect(self.hough)
        button30.clicked.connect(self.clear_label)
        button32.clicked.connect(self.face_detect)
        button33.clicked.connect(self.face_crop)
        button34.clicked.connect(self.mosaic)
        button35.clicked.connect(self.blur_mosaic)
     
        label0 = QLabel("이미지")
        label1 = QLabel("반전")
        label2 = QLabel("색변환")
        label3 = QLabel("크기조절")
        label4 = QLabel("회전")
        label5 = QLabel("변환")
        label6 = QLabel("왜곡")
        label7 = QLabel("블러")
        label8 = QLabel("경계검출")
        label9 = QLabel("영상분할")
        label10 = QLabel("얼굴")
        label11 = QLabel("모자이크")

        label0.setStyleSheet ("background-color: #E0E0E0")
        label0.setAlignment(Qt.AlignCenter)
        label0.setFont(QFont(" ", 11, QFont.Bold))
        label1.setStyleSheet ("background-color: #E0E0E0")
        label1.setAlignment(Qt.AlignCenter)
        label1.setFont(QFont(" ", 11, QFont.Bold))
        label2.setStyleSheet ("background-color: #E0E0E0")
        label2.setAlignment(Qt.AlignCenter)
        label2.setFont(QFont(" ", 11, QFont.Bold))
        label3.setStyleSheet ("background-color: #E0E0E0")
        label3.setAlignment(Qt.AlignCenter)
        label3.setFont(QFont(" ", 11, QFont.Bold))
        label4.setStyleSheet ("background-color: #E0E0E0")
        label4.setAlignment(Qt.AlignCenter)
        label4.setFont(QFont(" ", 11, QFont.Bold))
        label5.setStyleSheet ("background-color: #E0E0E0")
        label5.setAlignment(Qt.AlignCenter)
        label5.setFont(QFont(" ", 11, QFont.Bold))
        label6.setStyleSheet ("background-color: #E0E0E0")
        label6.setAlignment(Qt.AlignCenter)
        label6.setFont(QFont(" ", 11, QFont.Bold))
        label7.setStyleSheet ("background-color: #E0E0E0")
        label7.setAlignment(Qt.AlignCenter)
        label7.setFont(QFont(" ", 11, QFont.Bold))
        label8.setStyleSheet ("background-color: #E0E0E0")
        label8.setAlignment(Qt.AlignCenter)
        label8.setFont(QFont(" ", 11, QFont.Bold))
        label9.setStyleSheet ("background-color: #E0E0E0")
        label9.setAlignment(Qt.AlignCenter)
        label9.setFont(QFont(" ", 11, QFont.Bold))
        label10.setStyleSheet ("background-color: #E0E0E0")
        label10.setAlignment(Qt.AlignCenter)
        label10.setFont(QFont(" ", 11, QFont.Bold))
        label11.setStyleSheet ("background-color: #E0E0E0")
        label11.setAlignment(Qt.AlignCenter)
        label11.setFont(QFont(" ", 11, QFont.Bold))

        sidebar.addWidget(button0, 0, 0)
        sidebar.addWidget(button1, 2, 0)
        sidebar.addWidget(button2, 2, 1)
        sidebar.addWidget(button3, 2, 2)
        sidebar.addWidget(button4, 4, 0)
        sidebar.addWidget(button5, 6, 0)
        sidebar.addWidget(button6, 6, 1)
        sidebar.addWidget(button7, 8, 0)
        sidebar.addWidget(button8, 8, 1)
        sidebar.addWidget(button9, 8, 2)
        sidebar.addWidget(button10, 10, 0)
        sidebar.addWidget(button11, 10, 1)
        sidebar.addWidget(button12, 10, 2)
        sidebar.addWidget(button13, 12, 0)
        sidebar.addWidget(button14, 12, 1)
        sidebar.addWidget(button15, 12, 2)
        sidebar.addWidget(button16, 13, 0)
        sidebar.addWidget(button17, 13, 1)
        sidebar.addWidget(button18, 13, 2)
        sidebar.addWidget(button19, 16, 0)
        sidebar.addWidget(button20, 16, 1)
        sidebar.addWidget(button21, 17, 0)
        sidebar.addWidget(button22, 17, 1)
        sidebar.addWidget(button23, 19, 0)
        sidebar.addWidget(button24, 19, 1)
        sidebar.addWidget(button25, 19, 2)
        sidebar.addWidget(button26, 20, 0)
        sidebar.addWidget(button27, 20, 1)
        sidebar.addWidget(button28, 20, 2)
        sidebar.addWidget(button29, 22, 0)
        sidebar.addWidget(button31, 22, 1)
        sidebar.addWidget(button30, 0, 1)
        sidebar.addWidget(button32, 24, 0)
        sidebar.addWidget(button33, 24, 1)
        sidebar.addWidget(button34, 26, 0)
        sidebar.addWidget(button35, 26, 1)
      
        sidebar.addWidget(label0, -1, 0)
        sidebar.addWidget(label1, 1, 0)
        sidebar.addWidget(label2, 3, 0)
        sidebar.addWidget(label3, 5, 0)
        sidebar.addWidget(label4, 7, 0)
        sidebar.addWidget(label5, 9, 0)
        sidebar.addWidget(label6, 11, 0)
        sidebar.addWidget(label7, 15, 0)
        sidebar.addWidget(label8, 18, 0)
        sidebar.addWidget(label9, 21, 0)
        sidebar.addWidget(label10, 23,0)
        sidebar.addWidget(label11, 25, 0)

        main_layout.addLayout(sidebar)
        
        self.label1 = QLabel(self)
        self.label1.setFixedSize(640, 480)
        main_layout.addWidget(self.label1)

        self.label2 = QLabel(self)
        self.label2.setFixedSize(640, 480)
        main_layout.addWidget(self.label2)

        '''self.label3=QLabel(self)
        self.label3.setFixedSize(500,500)  #크기 고정
        main_layout.addWidget(self.label3)'''

        widget = QWidget(self)
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    
    #0 이미지 열기
    def show_file_dialog(self): 
        file_name = QFileDialog.getOpenFileName(self, "이미지 열기", "./")
        self.image = cv2.imread(file_name[0])
        h, w, _ = self.image.shape
        bytes_per_line = 3 * w
        image = QImage(
            self.image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label1.setPixmap(pixmap)


    #1 좌우반전
    def flip_LR_image(self):
        image = cv2.flip(self.image, 1)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    #2 상하반전
    def flip_updown_image(self):
        image = cv2.flip(self.image, 0)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    #3 상하좌우반전
    def flip_updown_LR_image(self):
        image = cv2.flip(self.image, -1)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    
    '''#5 BGR 변환
    def color_bgr(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)    #BGR->RGB로 변환
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)'''

    #4 흑백변환
    def color_gray(self):
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        h, w = image.shape
        bytes_per_line = 1 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_Grayscale8
        )
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap) 


    #5 확대
    def big(self):
        image = cv2.resize(self.image, None, None, 1.4, 1.4, cv2.INTER_CUBIC)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap) 

    #6 축소
    def small(self):
        image = cv2.resize(self.image, None, None, 0.5, 0.5, cv2.INTER_AREA)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap) 

    #7 45도회전
    def rotation_45(self):
        cp = (self.image.shape[1] / 2, self.image.shape[0] / 2) 
        rot = cv2.getRotationMatrix2D(cp, 45, 1)
        image = cv2.warpAffine(self.image, rot, (0, 0))
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap) 


    #8 90도 회전
    def rotation_90(self):
        cp = (self.image.shape[1] / 2, self.image.shape[0] / 2) 
        rot = cv2.getRotationMatrix2D(cp, 90, 1) 
        image = cv2.warpAffine(self.image, rot, (0, 0))
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    #9 축소회전
    def rotation_small(self):
        cp = (self.image.shape[1] / 2, self.image.shape[0] / 2) 
        rot = cv2.getRotationMatrix2D(cp, 20, 0.5) 
        image = cv2.warpAffine(self.image, rot, (0, 0))
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    #10 어핀변환
    def affine(self):
        aff = np.array([[1, 0.5, 0],
                [0, 1, 0]], dtype = np.float32)
        h, w = self.image.shape[:2]  
        image = cv2.warpAffine(self.image, aff, (w + int(h * 0.5), h))
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap) 

    #11 원근변환
    def perspective(self):
        rows, cols = self.image.shape[:2]
        pts1 = np.float32([[0, 0], [0, rows], [cols, 0], [cols, rows]])
        pts2 = np.float32([[100, 50], [10, rows - 50], [cols - 100, 50], [cols - 10, rows - 50]])
        mtrx = cv2.getPerspectiveTransform(pts1, pts2)
        image = cv2.warpPerspective(self.image, mtrx, (cols, rows))
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap) 
        

    #12 비선형변환
    def wave(self):
        l = 20
        amp = 15
        rows, cols = self.image.shape[:2]
        mapy, mapx = np.indices((rows, cols), dtype = np.float32)
        sinx = mapx + amp*np.sin(mapy/l)
        cosy = mapy + amp*np.cos(mapx/l)
        image = cv2.remap(self.image, sinx, cosy, cv2.INTER_LINEAR, None, cv2.BORDER_REPLICATE) 
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        
    #13 오목왜곡
    def distortion_concave(self):
        rows, cols = self.image.shape[:2]
        exp = 0.5
        scale = 1

        mapy, mapx = np.indices((rows,cols), dtype = np.float32)
        mapx = 2*mapx/(cols - 1) - 1
        mapy = 2*mapy/(rows - 1) - 1

        r, theta = cv2.cartToPolar(mapx, mapy)
        r[r < scale] = r[r < scale]**exp
        mapx, mapy = cv2.polarToCart(r, theta)
        mapx = ((mapx + 1)*cols - 1)/2
        mapy = ((mapy + 1)*rows - 1)/2
        image = cv2.remap(self.image, mapx, mapy, cv2.INTER_LINEAR)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    #14 볼록왜곡
    def distortion_convex(self):
        rows, cols = self.image.shape[:2]
        exp = 2
        scale = 1
        mapy, mapx = np.indices((rows, cols), dtype = np.float32)
        mapx = 2*mapx/(cols - 1) - 1
        mapy = 2*mapy/(rows - 1) - 1

        r, theta = cv2.cartToPolar(mapx, mapy)
        r[r< scale] = r[r< scale] **exp
        mapx, mapy = cv2.polarToCart(r, theta)
        mapx = ((mapx + 1)*cols - 1)/2
        mapy = ((mapy + 1)*rows - 1)/2
        image = cv2.remap(self.image, mapx, mapy, cv2.INTER_LINEAR)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    #15 핀쿠션왜곡
    def pincushion(self):
        k1, k2, k3 = -0.3, 0, 0 
        rows, cols = self.image.shape[:2]
        mapy, mapx = np.indices((rows, cols), dtype = np.float32)
        mapx = 2*mapx/(cols - 1) - 1
        mapy = 2*mapy/(rows - 1) - 1
        r, theta = cv2.cartToPolar(mapx, mapy)
        ru = r*(1+k1*(r**2) + k2*(r**4) + k3*(r**6)) 
        mapx, mapy = cv2.polarToCart(ru, theta)
        mapx = ((mapx + 1)*cols-1)/2
        mapy = ((mapy + 1)*rows-1)/2
        image = cv2.remap(self.image ,mapx, mapy, cv2.INTER_LINEAR)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    #16 배럴왜곡
    def barrel(self):
        k1, k2, k3 = 0.5, 0.2, 0.0 
        rows, cols = self.image.shape[:2]
        mapy, mapx = np.indices((rows, cols),dtype = np.float32)
        mapx = 2*mapx/(cols - 1) - 1
        mapy = 2*mapy/(rows - 1) - 1
        r, theta = cv2.cartToPolar(mapx, mapy)
        ru = r*(1+k1*(r**2) + k2*(r**4) + k3*(r**6)) 
        mapx, mapy = cv2.polarToCart(ru, theta)
        mapx = ((mapx + 1)*cols-1)/2
        mapy = ((mapy + 1)*rows-1)/2
        image = cv2.remap(self.image, mapx, mapy, cv2.INTER_LINEAR)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
    
    #17 좌우거울왜곡
    def mirror_LR(self):
        rows, cols = self.image.shape[:2]
        map_y, map_x = np.indices((rows, cols), dtype = np.float32)
        map_mirrorh_x, map_mirrorh_y = map_x.copy(), map_y.copy()
        map_mirrorh_x[:, cols//2:] = cols-map_mirrorh_x[:, cols//2:] - 1
        image = cv2.remap(self.image, map_mirrorh_x, map_mirrorh_y, cv2.INTER_LINEAR)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)


    #18 상하거울왜곡
    def mirror_UD(self):
        rows, cols = self.image.shape[:2]
        map_y, map_x = np.indices((rows, cols), dtype = np.float32)
        map_mirrorv_x, map_mirrorv_y = map_x.copy(), map_y.copy()
        map_mirrorv_y[rows//2:, :] = rows - map_mirrorv_y[rows//2: , :] - 1
        image = cv2.remap(self.image, map_mirrorv_x, map_mirrorv_y, cv2.INTER_LINEAR)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    #19 평균블러링
    def blur(self):
        kernel = np.array([[0.04,0.04,0.04,0.04,0.04],
                   [0.04,0.04,0.04,0.04,0.04],
                   [0.04,0.04,0.04,0.04,0.04],
                   [0.04,0.04,0.04,0.04,0.04],
                   [0.04,0.04,0.04,0.04,0.04]])
        kernel = np.ones((5,5))/5**2
        image = cv2.filter2D(self.image, -1, kernel)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)    

    #20 가우시안블러링
    def gaussian(self):
        kernel = np.array([
            [1, 2, 1],
            [2, 4, 2],
            [1, 2, 1]
        ]) * (1/16)        
        image = cv2.filter2D(self.image, -1, kernel)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap) 

    #21 미디언블러링
    def median(self):
        image = cv2.medianBlur(self.image, 5)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap) 
        

    #22 바이레터럴 블러링
    def bilateral(self):
        image = cv2.bilateralFilter(self.image, 5, 75, 75)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
    
    #23 기본미분
    def differential(self):
        gx_kernel = np.array([[-1, 1]])
        gy_kernel = np.array([[-1], [1]])

        edge_gx = cv2.filter2D(self.image, -1, gx_kernel)
        edge_gy = cv2.filter2D(self.image, -1, gy_kernel)

        image = edge_gx + edge_gy
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    #24 로버츠교차
    def roberts(self):
        gx_kernel = np.array([[1, 0], [0, -1]])
        gy_kernel = np.array([[0, 1], [-1, 0]])

        edge_gx = cv2.filter2D(self.image, -1, gx_kernel)
        edge_gy = cv2.filter2D(self.image, -1, gy_kernel)

        image = edge_gx + edge_gy
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
    
    #25 캐니엣지
    def canny(self):
        image = cv2.Canny(self.image, 100, 200)
        h, w = image.shape
        bytes_per_line = 1 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_Grayscale8
        )
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    #26 프리윗 
    def prewitt(self):
        gx_kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        gy_kernel = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
        edge_gx = cv2.filter2D(self.image, -1, gx_kernel)
        edge_gy = cv2.filter2D(self.image, -1, gy_kernel)
        image = edge_gx + edge_gy
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    #27 소벨
    def sobel(self):
        gx_kernel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
        gy_kernel = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
        edge_gx = cv2.filter2D(self.image, -1, gx_kernel)
        edge_gy = cv2.filter2D(self.image, -1, gy_kernel)
        image = edge_gx + edge_gy
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
    
    #28 라플라시안
    def laplacian(self):
        image = cv2.Laplacian(self.image, -1)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)

    #29 컨투어
    def contour(self):
        image = self.image.copy()
        img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, img_thresh = cv2.threshold(
            img_gray, 127, 255, cv2.THRESH_BINARY_INV
        )
        contour, hierarchy = cv2.findContours(
            img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )
        cv2.drawContours(image, contour, -1, (255, 0, 0), 4)
        h, w, _ = image.shape
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap)
        
    #31 허프 선 변환
    def hough(self):
        image = self.image.copy()
        h, w = self.image.shape[:2]
        img_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(img_gray, 50, 200)
        lines = cv2.HoughLines(edges, 1, np.pi/180, 130)

        for line in lines:
            r, theta = line[0]
            tx, ty = np.cos(theta), np.sin(theta)
            x0, y0 = tx*r, ty*r
            x1, y1 = int(x0 + w*(-ty)), int(y0 + h * tx)
            x2, y2 = int(x0 - w*(-ty)), int(y0 - h * tx)
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 1)
        
        bytes_per_line = 3 * w
        image = QImage(
            image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image)
        self.label2.setPixmap(pixmap) 
    
    #32 얼굴인식
    def face_detect(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(image)
        for (x, y, w, h) in faces:
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 2)    
        cv2.imshow('face',self.image)
        cv2.moveWindow('face', 1000, 300)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #33 얼굴자르기
    def face_crop(self):
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cropped = self.image[y - int(h/4):y + h + int(h/4), x - int(w/4):x + w + int(w/4)]
        cv2.imshow('copped_image', cropped)
        cv2.moveWindow('copped_image', 1000, 300)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    #34 모자이크
    def mosaic(self):
        rate = 15
        title = 'mosaic'
        x, y, w, h = cv2.selectROI(title, self.image, False)
        roi = self.image[y:y+h, x:x+w]
        roi = cv2.resize(roi, (w//rate, h//rate))
        roi = cv2.resize(roi, (w, h), interpolation = cv2.INTER_AREA)
        image1 = self.image
        image1[y:y+h, x:x+w] = roi
        h, w, _ = self.image.shape
        bytes_per_line = 3 * w
        image1 = QImage(
            self.image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image1)
        self.label2.setPixmap(pixmap)

    #35 블러모자이크
    def blur_mosaic(self):
        ksize = 30             
        title = 'blur_mosaic'    
        x, y, w, h = cv2.selectROI(title, self.image, False)   
        roi = self.image[y:y+h, x:x+w]   
        roi = cv2.blur(roi, (ksize, ksize)) 
        image = self.image
        image[y:y+h, x:x+w] = roi  
        h, w, _ = self.image.shape
        bytes_per_line = 3 * w
        image1 = QImage(
            self.image.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()
        pixmap = QPixmap(image1)
        self.label2.setPixmap(pixmap)
    
    #30 새로고침
    def clear_label(self):
        self.label2.clear()
        self.label3.clear()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    
if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

