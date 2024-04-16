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
        uic.loadUi('./myUi.ui', self)
        self.printTable()
        self.func()

    def printTable(self):
        db= connectDb()
        db[1].execute('select * from INFO')
        result= db[1].fetchall()
        count = len(result)
        self.tableWidget.setRowCount(count)
        for x in range(count):
            idx, name, tel = result[x]
            self.tableWidget.setItem(x,0,QTableWidgetItem(idx))
            self.tableWidget.setItem(x,1,QTableWidgetItem(name))
            self.tableWidget.setItem(x,2,QTableWidgetItem(tel))

    ## 버튼 클릭할때의 동작
    def func(self):
        self.btnCol.clicked.connect(self.btnColClicked)
        self.btnAdd.clicked.connect(self.btnAddClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)
        self.btnDelete.clicked.connect(self.btnDeleteClicked)
        self.tableWidget.cellClicked.connect(self.cellClicked)

    ## 행 추가
    def btnColClicked(self):
        self.tableWidget.insertRow(0)

    ## 신규 등록
    def btnAddClicked(self):
        idx = self.tableWidget.item(0,0).text()
        name = self.tableWidget.item(0,1).text()
        tel = self.tableWidget.item(0,2).text()
        db= connectDb()
        db[1].execute(f"insert into INFO (ID, NAME, TEL) values ('{idx}','{name}','{tel}')")
        db[1].execute('commit')

    ## DB 수정
    def btnSaveClicked(self):
        rowCount = self.tableWidget.rowCount()
        for i in range(rowCount):
            idx = self.tableWidget.item(i,0).text()
            name = self.tableWidget.item(i,1).text()
            tel = self.tableWidget.item(i,2).text()
            db= connectDb()
            db[1].execute(f"update INFO set NAME= '{name}', TEL= '{tel}' where ID= '{idx}'")
            db[1].execute('commit')

    ## 삭제
    def btnDeleteClicked(self):
        row = self.rownum
        idx = self.tableWidget.item(row,0).text()
        db= connectDb()
        db[1].execute(f"delete from INFO where ID = '{idx}'")
        db[1].execute('commit')
        self.printTable()

    ## 마우스로 클릭하면 해당 셀의 행의 데이터 값들 출력
    def cellClicked(self, row):
        self.rownum = row

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