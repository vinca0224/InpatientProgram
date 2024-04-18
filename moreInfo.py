import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import oracledb as odb
from PyQt5.QtGui import *

class MoreInfo(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./moreInfo.ui', self)
        self.setWindowTitle('상세정보')
        self.setWindowIcon(QIcon('icon.png'))

## 메인 메소드 실행
if __name__ == '__main__':
    app = QApplication(sys.argv)
    info = MoreInfo()
    info.show()
    sys.exit(app.exec_())