import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QWidget
import oracledb as odb
from register import RegisterInfo
from moreInfo import MoreInfo

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./myUi.ui', self)
        self.setWindowTitle('inpatient program v0.1')
        self.setWindowIcon(QIcon('icon.png'))
        self.printTable()
        self.func()

    ## 표 출력
    def printTable(self):
        db= connectDb()
        db[1].execute('select * from INFO')
        result= db[1].fetchall()
        count = len(result)
        self.tableWidget.setRowCount(count)
        for x in range(count):
            idx, name, tel, room, date, dept, desc = result[x]
            ### datetime 타입을 str로 변환
            date = str(date).split(' ')[0]
            self.tableWidget.setItem(x,0,QTableWidgetItem(idx))
            self.tableWidget.setItem(x,1,QTableWidgetItem(name))
            self.tableWidget.setItem(x,2,QTableWidgetItem(tel))
            self.tableWidget.setItem(x,3,QTableWidgetItem(room))
            self.tableWidget.setItem(x,4,QTableWidgetItem(date))
            self.tableWidget.setItem(x,5,QTableWidgetItem(dept))
            self.tableWidget.setItem(x,6,QTableWidgetItem(desc))
        self.disableColumnSelection(0) # ID = 0

    ## ID 컬럼은 수정할 수 없도록 제한
    def disableColumnSelection(self, column):
        for row in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(row, column)
            if item:
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)

    ## 버튼 클릭할때의 동작
    def func(self):
        self.btnRenew.clicked.connect(self.btnRenewed)
        self.btnCol.clicked.connect(self.btnAddClicked)
        self.btnSave.clicked.connect(self.btnSaveClicked)
        self.btnDelete.clicked.connect(self.btnDeleteClicked)
        self.btnSearch.clicked.connect(self.btnSearched)
        self.tableWidget.cellClicked.connect(self.cellClicked)

    ## 조회
    def btnRenewed(self):
        self.printTable()

    ## 등록
    def btnAddClicked(self):
        self.register = RegisterInfo()
        self.register.show()

    ## DB 수정
    def btnSaveClicked(self):
        re = QMessageBox.question(self, '수정', '수정하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes: # 종료
            try:
                row = self.rownum
                idx = self.tableWidget.item(row,0).text()
                name = self.tableWidget.item(row,1).text()
                tel = self.tableWidget.item(row,2).text()
                room = self.tableWidget.item(row,3).text()
                date = self.tableWidget.item(row,4).text()
                dept = self.tableWidget.item(row,5).text()
                ### 비고는 공백 가능
                try:
                    desc = self.tableWidget.item(row,6).text()
                except: desc = ' '
                db= connectDb()
                db[1].execute(f"update INFO set NAME= '{name}', TEL= '{tel}', ROOM= '{room}', DAY= '{date}', DEPT= '{dept}', DC= '{desc}' where ID= '{idx}'")
                db[1].execute('commit')
                QMessageBox.about(self,'수정 성공','수정하였습니다.')
            except AttributeError:
                pass
            except: 
                QMessageBox.about(self,'에러','오류가 발생하였습니다')
        else:
            QMessageBox.about(self,'취소','취소되었습니다.') 
            pass

    ## 삭제
    def btnDeleteClicked(self):
        re = QMessageBox.question(self, '경고', '삭제하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes: # 종료
            try:
                row = self.rownum
                idx = self.tableWidget.item(row,0).text()
                db= connectDb()
                db[1].execute(f"delete from INFO where ID = '{idx}'")
                db[1].execute('commit')
                self.printTable()
            except: pass
        else:
            QMessageBox.about(self,'취소','취소되었습니다.')
            pass
    
    ## 검색
    def btnSearched(self):
        searchText = self.lineSearch.text()
        db= connectDb()
        db[1].execute(f"select * from INFO where id= '{searchText}' or name = '{searchText}'")
        result= db[1].fetchall()
        count = len(result)
        self.tableWidget.setRowCount(count)
        for x in range(count):
            idx, name, tel, room, date, dept, desc = result[x]
            ### datetime 타입을 str로 변환
            date = str(date).split(' ')[0]
            self.tableWidget.setItem(x,0,QTableWidgetItem(idx))
            self.tableWidget.setItem(x,1,QTableWidgetItem(name))
            self.tableWidget.setItem(x,2,QTableWidgetItem(tel))
            self.tableWidget.setItem(x,3,QTableWidgetItem(room))
            self.tableWidget.setItem(x,4,QTableWidgetItem(date))
            self.tableWidget.setItem(x,5,QTableWidgetItem(dept))
            self.tableWidget.setItem(x,6,QTableWidgetItem(desc))
        self.disableColumnSelection(0) # ID = 0

    ## 마우스로 클릭하면 해당 셀의 행의 데이터 값들 출력
    def cellClicked(self, row):
        self.rownum = row

    def keyPressEvent(self, input):
        if input.key() == Qt.Key_Return:
            self.info = MoreInfo()
            self.info.show()

    ## 종료
    def closeEvent(self, QCloseEvent) -> None: # 오버라이딩
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 종료
            
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() # 취소

## DB와 연결
def connectDb():
    conn= odb.connect(user= 'ADAM', password='1234', dsn='localhost:1521/XE')
    cursor= conn.cursor() # DB 지시자
    return conn, cursor

## 메인 메소드 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWidget = MainWidget()
    mainWidget.show()
    sys.exit(app.exec_())