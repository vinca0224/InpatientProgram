import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import oracledb as odb
from PyQt5.QtGui import *

class CreateUser(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./create.ui', self)
        self.setWindowTitle('계정 생성')
        self.setWindowIcon(QIcon('icon.png'))
        self.btnCreate.clicked.connect(self.btnCreateClicked)

    ## 회원가입
    def btnCreateClicked(self):
        id = self.lineId.text()
        pw = self.linePw.text()
        try:
            db = connectDb()
            db[1].execute(f"insert into myuser (id, pw) values ('{id}', '{pw}')")
            db[1].execute('commit')
            QMessageBox.about(self, '가입 완료', '계정을 생성하였습니다.')
            self.close()
        except: QMessageBox.about(self, '오류', '이미 존재하는 ID입니다')

## DB와 연결
def connectDb():
    conn= odb.connect(user= 'ADAM', password='1234', dsn='localhost:1521/XE')
    cursor= conn.cursor() # DB 지시자
    return conn, cursor

## 메인 메소드 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    createUser = CreateUser()
    createUser.show()
    sys.exit(app.exec_())