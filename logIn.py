import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import oracledb as odb
from PyQt5.QtGui import *
from menu import MainWidget
from createUser import CreateUser

class LogIn(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./logIn.ui', self)
        self.setWindowTitle('로그인')
        self.setWindowIcon(QIcon('icon.png'))
        self.btnLogIn.clicked.connect(self.btnLogInClicked)
        self.btnRegister.clicked.connect(self.btnRegisterClicked)

    
    ## 로그인
    def btnLogInClicked(self):
        id = self.lineId.text()
        pw = self.linePw.text()
        try:
            db = connectDb()
            db[1].execute(f"Select * from MYUSER where id = '{id}' and pw = '{pw}'")
            result = db[1].fetchall()
            if len(result) > 0:
                self.menu = MainWidget()
                self.menu.show()
                self.close()
            else: QMessageBox.about(self, '오류', 'ID와 PW를 확인해 주세요')
        except: QMessageBox.about(self, '오류', 'ID와 PW를 확인해 주세요')

    ## 회원가입 - db 사용자 생성
    def btnRegisterClicked(self) :
        pass
        self.createUser = CreateUser()
        self.createUser.show()

def connectDb():
    conn= odb.connect(user= 'ADAM', password = '1234', dsn='localhost:1521/XE')
    cursor= conn.cursor() # DB 지시자
    return conn, cursor

## 메인 메소드 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    logIn = LogIn()
    logIn.show()
    sys.exit(app.exec_())