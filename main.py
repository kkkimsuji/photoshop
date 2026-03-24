import sys
import cv2
import numpy as np
from PySide6.QtGui import QAction, QImage, QPixmap, QFont, Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow, 
    QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog, QGridLayout, QScrollArea
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Photoshop - Refactored")
        self.image = None  # 원본 이미지 저장용
        
        self.init_menu()
        self.init_ui()

    def init_menu(self):
        """메뉴바 초기화"""
        menu = self.menuBar()
        menu.setNativeMenuBar(False)

        # 파일 메뉴
        file_menu = menu.addMenu("파일")
        actions = [
            ("새로 만들기", "Ctrl+N", None),
            ("열기", "Ctrl+O", self.show_file_dialog),
            ("저장", "Ctrl+S", None),
            ("나가기", None, self.close)
        ]
        for text, shortcut, slot in actions:
            action = QAction(text, self)
            if shortcut: action.setShortcut(shortcut)
            if slot: action.triggered.connect(slot)
            file_menu.addAction(action)

        # 제출자 정보 (간소화)
        me_menu = menu.addMenu("제출자")
        for info in ["IT융합공학과", "2020101462", "김수지"]:
            me_menu.addAction(QAction(info, self))

    def init_ui(self):
        """메인 레이아웃 및 버튼 자동 생성"""
        main_layout = QHBoxLayout()
        
        # 사이드바 레이아웃 (스크롤 가능하게 설정하면 버튼이 많아도 안전합니다)
        sidebar_layout = QGridLayout()
        
        # 버튼 구성 데이터 (텍스트: 슬롯 메서드)
        button_groups = {
            "이미지": [("이미지 열기", self.show_file_dialog), ("새로고침", self.clear_label)],
            "반전": [("좌우반전", lambda: self.process_image(cv2.flip, 1)), 
                     ("상하반전", lambda: self.process_image(cv2.flip, 0)), 
                     ("상하좌우", lambda: self.process_image(cv2.flip, -1))],
            "변환": [("흑백변환", self.color_gray), ("확대", self.big), ("축소", self.small)],
            "회전": [("45도", self.rotation_45), ("90도", self.rotation_90)],
            "왜곡/필터": [("원근변환", self.perspective), ("비선형", self.wave), ("오목", self.distortion_concave), 
                         ("볼록", self.distortion_convex), ("평균블러", self.blur), ("가우시안", self.gaussian)],
            "엣지/분할": [("Canny", self.canny), ("Sobel", self.sobel), ("컨투어", self.contour)],
            "인공지능/기타": [("얼굴인식", self.face_detect), ("모자이크", self.mosaic)]
        }

        row = 0
        for category, buttons in button_groups.items():
            # 카테고리 라벨 생성
            cat_label = QLabel(category)
            cat_label.setStyleSheet("background-color: #E0E0E0; font-weight: bold; padding: 5px;")
            cat_label.setAlignment(Qt.AlignCenter)
            sidebar_layout.addWidget(cat_label, row, 0, 1, 3)
            row += 1
            
            # 버튼들 배치
            col = 0
            for text, slot in buttons:
                btn = QPushButton(text)
                btn.clicked.connect(slot)
                sidebar_layout.addWidget(btn, row, col)
                col += 1
                if col > 2: # 3열 배치
                    col = 0
                    row += 1
            row += 1

        main_layout.addLayout(sidebar_layout)
        
        # 이미지 표시 라벨
        self.label_origin = QLabel("원본 이미지")
        self.label_result = QLabel("결과 이미지")
        for lbl in [self.label_origin, self.label_result]:
            lbl.setFixedSize(640, 480)
            lbl.setAlignment(Qt.AlignCenter)
            lbl.setStyleSheet("border: 1px solid black; background-color: #F0F0F0;")
            main_layout.addWidget(lbl)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    # --- 공통 유틸리티 메서드 ---
    def display_image(self, img, target_label):
        """OpenCV 이미지를 Qt 라벨에 표시하는 핵심 메서드"""
        if img is None: return
        
        if len(img.shape) == 2: # 흑백 이미지 처리
            h, w = img.shape
            q_img = QImage(img.data, w, h, w, QImage.Format_Grayscale8)
        else: # 컬러 이미지 처리
            h, w, c = img.shape
            q_img = QImage(img.data, w, h, w * c, QImage.Format_RGB888).rgbSwapped()
            
        pixmap = QPixmap.fromImage(q_img)
        target_label.setPixmap(pixmap.scaled(target_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def process_image(self, func, *args, **kwargs):
        """대부분의 단일 변환 함수를 처리하는 래퍼"""
        if self.image is None: return
        result = func(self.image.copy(), *args, **kwargs)
        self.display_image(result, self.label_result)

    # --- 기능 구현 메서드 ---
    def show_file_dialog(self): 
        fname, _ = QFileDialog.getOpenFileName(self, "이미지 열기", "./")
        if fname:
            self.image = cv2.imread(fname)
            self.display_image(self.image, self.label_origin)
            self.label_result.clear()

    def color_gray(self):
        if self.image is None: return
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.display_image(gray, self.label_result)

    def big(self):
        self.process_image(cv2.resize, None, fx=1.4, fy=1.4, interpolation=cv2.INTER_CUBIC)

    def small(self):
        self.process_image(cv2.resize, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    def rotation_45(self):
        if self.image is None: return
        h, w = self.image.shape[:2]
        cp = (w / 2, h / 2)
        rot = cv2.getRotationMatrix2D(cp, 45, 1)
        res = cv2.warpAffine(self.image, rot, (w, h))
        self.display_image(res, self.label_result)

    def rotation_90(self):
        if self.image is None: return
        res = cv2.rotate(self.image, cv2.ROTATE_90_CLOCKWISE)
        self.display_image(res, self.label_result)

    def perspective(self):
        if self.image is None: return
        rows, cols = self.image.shape[:2]
        pts1 = np.float32([[0, 0], [0, rows], [cols, 0], [cols, rows]])
        pts2 = np.float32([[100, 50], [10, rows - 50], [cols - 100, 50], [cols - 10, rows - 50]])
        mtrx = cv2.getPerspectiveTransform(pts1, pts2)
        res = cv2.warpPerspective(self.image, mtrx, (cols, rows))
        self.display_image(res, self.label_result)

    def wave(self):
        if self.image is None: return
        rows, cols = self.image.shape[:2]
        mapy, mapx = np.indices((rows, cols), dtype=np.float32)
        sinx = mapx + 15 * np.sin(mapy / 20)
        cosy = mapy + 15 * np.cos(mapx / 20)
        res = cv2.remap(self.image, sinx, cosy, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
        self.display_image(res, self.label_result)

    def distortion_concave(self):
        if self.image is None: return
        rows, cols = self.image.shape[:2]
        mapy, mapx = np.indices((rows, cols), dtype=np.float32)
        mapx = 2 * mapx / (cols - 1) - 1
        mapy = 2 * mapy / (rows - 1) - 1
        r, theta = cv2.cartToPolar(mapx, mapy)
        r[r < 1] = r[r < 1] ** 0.5
        mapx, mapy = cv2.polarToCart(r, theta)
        mapx = ((mapx + 1) * cols - 1) / 2
        mapy = ((mapy + 1) * rows - 1) / 2
        res = cv2.remap(self.image, mapx, mapy, cv2.INTER_LINEAR)
        self.display_image(res, self.label_result)

    def distortion_convex(self):
        if self.image is None: return
        rows, cols = self.image.shape[:2]
        mapy, mapx = np.indices((rows, cols), dtype=np.float32)
        mapx = 2 * mapx / (cols - 1) - 1
        mapy = 2 * mapy / (rows - 1) - 1
        r, theta = cv2.cartToPolar(mapx, mapy)
        r[r < 1] = r[r < 1] ** 2
        mapx, mapy = cv2.polarToCart(r, theta)
        mapx = ((mapx + 1) * cols - 1) / 2
        mapy = ((mapy + 1) * rows - 1) / 2
        res = cv2.remap(self.image, mapx, mapy, cv2.INTER_LINEAR)
        self.display_image(res, self.label_result)

    def blur(self):
        self.process_image(cv2.blur, (5, 5))

    def gaussian(self):
        self.process_image(cv2.GaussianBlur, (5, 5), 0)

    def canny(self):
        if self.image is None: return
        res = cv2.Canny(self.image, 100, 200)
        self.display_image(res, self.label_result)

    def sobel(self):
        if self.image is None: return
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        res = cv2.magnitude(sx, sy)
        res = np.uint8(np.clip(res, 0, 255))
        self.display_image(res, self.label_result)

    def contour(self):
        if self.image is None: return
        img_copy = self.image.copy()
        gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(img_copy, contours, -1, (255, 0, 0), 4)
        self.display_image(img_copy, self.label_result)

    def face_detect(self):
        if self.image is None: return
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        img_copy = self.image.copy()
        gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img_copy, (x, y), (x + w, y + h), (255, 0, 0), 2)
        self.display_image(img_copy, self.label_result)

    def mosaic(self):
        if self.image is None: return
        img_copy = self.image.copy()
        x, y, w, h = cv2.selectROI("Select ROI", img_copy, False)
        if w > 0 and h > 0:
            roi = img_copy[y:y+h, x:x+w]
            roi = cv2.resize(roi, (w//15, h//15))
            roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_AREA)
            img_copy[y:y+h, x:x+w] = roi
            self.display_image(img_copy, self.label_result)
        cv2.destroyWindow("Select ROI")

    def clear_label(self):
        self.label_result.clear()
        self.label_result.setText("결과 이미지")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
