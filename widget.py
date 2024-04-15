import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import oracledb as db
import func

#화면을 띄우는데 사용되는 Class 선언
class qtApp(QWidget) :
    def __init__(self) -> None:
        super().__init__()
        self.initUi()

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
    def initUi(self):
        uic.loadUi('./main.ui', self)

        self.btnRegister.clicked.connect(self.btnRegisterClicked) # 등록
        self.btnSearch.clicked.connect(self.btnSearchClicked) # 조회
        self.btnModify.clicked.connect(self.btnModifyClicked) # 수정
        self.btnDelete.clicked.connect(self.btnDeleteCLicked) # 종료
        self.show() # 윈도우 창 그리기
    
    def btnRegisterClicked(self):
        QMessageBox.about(self, '등록', '등록')

    def btnSearchClicked(self):
        QMessageBox.about(self, '조회', '조회')

    def btnModifyClicked(self):
        QMessageBox.about(self, '수정', '수정')

    def btnDeleteCLicked(self):
        QMessageBox.about(self, '삭제', '삭제')

    def closeEvent(self, QCloseEvent) -> None: # 오버라이딩
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 종료
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() # 취소

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 
    #인스턴스 생성
    inst = qtApp() 
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()