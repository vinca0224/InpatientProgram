import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import oracledb as db
from PyQt5.QtGui import *

class RegisterInfo(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./register.ui', self)
        self.setWindowTitle('환자 등록')
        self.setWindowIcon(QIcon('icon.png'))
        self.tableWidget.insertRow(0)
        self.btnAdd.clicked.connect(self.btnAddClicked)

    ## 신규 등록
    def btnAddClicked(self):
        re = QMessageBox.question(self, '등록', '등록하시겠습니까?', QMessageBox.Yes | QMessageBox.No)
        if re == QMessageBox.Yes: # 종료
            try:
                idx = self.tableWidget.item(0,0).text()
                name = self.tableWidget.item(0,1).text()
                tel = self.tableWidget.item(0,2).text()
                room = self.tableWidget.item(0,3).text()
                date = self.tableWidget.item(0,4).text()
                dept = self.tableWidget.item(0,5).text()
                ### 비고는 공백 가능
                try:
                    desc = self.tableWidget.item(0,6).text()
                except: desc = ' '
                db= connectDb()
                db[1].execute(f"insert into INFO (ID, NAME, TEL, ROOM, DEPT, DAY, DC) values ('{idx}','{name}','{tel}','{room}','{dept}','{date}','{desc}')")
                db[1].execute('commit')
                self.eventMsg('성공', '저장되었습니다')
            except AttributeError: 
                self.eventMsg('실패', '공백을 남기지 마세요')
                pass
            except:
                self.eventMsg('실패', '동일한 ID가 존재합니다')
                pass
        else:
            QMessageBox.about(self,'취소','취소되었습니다.')
            pass
    
    ## 메시지 박스
    def eventMsg(self, event, des):
        QMessageBox.about(self,f'{event}',f'{des}')

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    register = RegisterInfo()
    register.show()
    sys.exit(app.exec_())