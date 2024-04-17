import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import oracledb as db

class MainWindow(QMainWindow):   
    def __init__(self):
        global aaa
        super().__init__()
        aaa= uic.loadUi('./myUi.ui', self)
        self.setWindowTitle('환자관리')
        connectDb()
        self.mainUi()

    def mainUi(self):
        aaa.btnRegister.clicked.connect(aaa.btnRegisterClicked) # 등록
        aaa.btnModify.clicked.connect(aaa.btnModifyClicked) # 수정
        aaa.btnDelete.clicked.connect(aaa.btnDeleteCLicked) # 종료

    def btnRegisterClicked(self):
        aaa.tableWidget.insertRow(1)
        
        
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

## DB에 연결
def connectDb():
    con = db.connect(user= 'ADAM', password='1234', dsn='localhost:1521/XE')
    cursor = con.cursor() #DB 지시자
    cursor.execute('select * from INFO')
    result= cursor.fetchall()
    setTable(result)
    
## 테이블에 출력
def setTable(row):
    count = len(row)
    aaa.tableWidget.setRowCount(count)
    for x in range(count):
        idx, name, tel = row[x]
        aaa.tableWidget.setItem(x,0,QTableWidgetItem(idx))
        aaa.tableWidget.setItem(x,1,QTableWidgetItem(name))
        aaa.tableWidget.setItem(x,2,QTableWidgetItem(tel))
        

if __name__ == '__main__':
    app= QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
