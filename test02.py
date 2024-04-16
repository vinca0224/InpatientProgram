import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
import oracledb as db

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.menu()
        self.func()

    def menu(self):
        uic.loadUi('./myUi.ui', self)
        db= connectDb()
        db[1].execute('select * from INFO')
        result= db[1].fetchall()
        self.printTable(result)

    def printTable(self, row):
        count = len(row)
        self.tableWidget.setRowCount(count)
        for x in range(count):
            idx, name, tel = row[x]
            self.tableWidget.setItem(x,0,QTableWidgetItem(idx))
            self.tableWidget.setItem(x,1,QTableWidgetItem(name))
            self.tableWidget.setItem(x,2,QTableWidgetItem(tel))

    def func(self):
        self.btnAdd.clicked.connect(self.btnAddClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)
        self.btnDelete.clicked.connect(self.btnDeleteClicked)

    ## 행 추가
    def btnAddClicked(self):
        self.tableWidget.insertRow(0)

    ## DB 저장
    def btnSaveClicked(self):
        rowCount = self.tableWidget.rowCount()
        for i in range(rowCount):
            idx = self.tableWidget.item(i,0).text()
            name = self.tableWidget.item(i,1).text()
            tel = self.tableWidget.item(i,2).text()
            print(idx, name, tel)

    ## 삭제
    def btnDeleteClicked(self):
        pass
    
    ## 종료
    def closeEvent(self, QCloseEvent) -> None: # 오버라이딩
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 종료
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() # 취소

## DB와 연결
def connectDb():
    conn= db.connect(user= 'ADAM', password='1234', dsn='localhost:1521/XE')
    cursor= conn.cursor() # DB 지시자
    return conn, cursor

## 메인 메소드 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidget = MainWidget()
    mainWidget.show()
    sys.exit(app.exec_())