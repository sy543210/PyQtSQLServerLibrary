import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import qdarkstyle
from PyQt5.QtSql import *
from lib.SQLQuery import MSSQL


class BorrowStatusViewer(QWidget):
    def __init__(self, studentId):
        super(BorrowStatusViewer, self).__init__()
        self.resize(2000, 700)
        self.studentId = int(studentId)
        self.setWindowTitle("欢迎使用YU图书馆管理系统")
        self.setUpUI()

    def setUpUI(self):
        # 分为两块，上方是已借未归还书，下方是已归还书
        self.layout = QVBoxLayout(self)
        # Label设置
        self.borrowedLabel = QLabel("未归还:")
        self.returnedLabel = QLabel("已归还:")
        self.borrowedLabel.setFixedHeight(32)
        self.borrowedLabel.setFixedWidth(60)
        self.returnedLabel.setFixedHeight(32)
        self.returnedLabel.setFixedWidth(60)
        font = QFont()
        font.setPixelSize(18)
        self.borrowedLabel.setFont(font)
        self.returnedLabel.setFont(font)

        # Table和Model
        self.borrowedTableView = QTableView()
        self.borrowedTableView.horizontalHeader().setStretchLastSection(True)
        self.borrowedTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.borrowedTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.returnedTableView = QTableView()
        self.returnedTableView.horizontalHeader().setStretchLastSection(True)
        self.returnedTableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.returnedTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.borrowedQueryModel = QStandardItemModel(12,12)
        self.returnedQueryModel = QStandardItemModel(12,12)
        self.borrowedTableView.setModel(self.borrowedQueryModel)
        self.returnedTableView.setModel(self.returnedQueryModel)
        self.borrowedQuery()
        self.borrowedQueryModel.setHeaderData(0, Qt.Horizontal, "借书号")
        self.borrowedQueryModel.setHeaderData(1, Qt.Horizontal, "读者号号")
        self.borrowedQueryModel.setHeaderData(2, Qt.Horizontal, "书号")
        self.borrowedQueryModel.setHeaderData(3, Qt.Horizontal, "续借时间")
        self.borrowedQueryModel.setHeaderData(4, Qt.Horizontal, "借书时间")
        self.borrowedQueryModel.setHeaderData(5, Qt.Horizontal, "预计归还时间")
        self.borrowedQueryModel.setHeaderData(6, Qt.Horizontal, "实际归还时间")
        self.borrowedQueryModel.setHeaderData(7, Qt.Horizontal, "超期时间")
        self.borrowedQueryModel.setHeaderData(8, Qt.Horizontal, "超期罚金")
        self.borrowedQueryModel.setHeaderData(9, Qt.Horizontal, "罚金")
        self.borrowedQueryModel.setHeaderData(10, Qt.Horizontal, "是否归还")
        self.borrowedQueryModel.setHeaderData(11, Qt.Horizontal, "借书操作人")
        self.borrowedQueryModel.setHeaderData(12, Qt.Horizontal, "还书操作人")


        self.returnedQuery()
        self.returnedQueryModel.setHeaderData(13, Qt.Horizontal, "借书号")
        self.returnedQueryModel.setHeaderData(1, Qt.Horizontal, "读者号号")
        self.returnedQueryModel.setHeaderData(2, Qt.Horizontal, "书号")
        self.returnedQueryModel.setHeaderData(3, Qt.Horizontal, "续借时间")
        self.returnedQueryModel.setHeaderData(4, Qt.Horizontal, "借书时间")
        self.returnedQueryModel.setHeaderData(5, Qt.Horizontal, "预计归还时间")
        self.returnedQueryModel.setHeaderData(6, Qt.Horizontal, "实际归还时间")
        self.returnedQueryModel.setHeaderData(7, Qt.Horizontal, "超期时间")
        self.returnedQueryModel.setHeaderData(8, Qt.Horizontal, "超期罚金")
        self.returnedQueryModel.setHeaderData(9, Qt.Horizontal, "罚金")
        self.returnedQueryModel.setHeaderData(10, Qt.Horizontal, "是否归还")
        self.returnedQueryModel.setHeaderData(11, Qt.Horizontal, "借书操作人")
        self.returnedQueryModel.setHeaderData(12, Qt.Horizontal, "还书操作人")

        self.layout.addWidget(self.borrowedLabel)
        self.layout.addWidget(self.borrowedTableView)
        self.layout.addWidget(self.returnedLabel)
        self.layout.addWidget(self.returnedTableView)
        return

    def borrowedQuery(self):
        sql = f"SELECT * FROM TB_Borrow WHERE rdID={self.studentId} AND IsHasReturn=0"
        Library = MSSQL('Library')
        borrowresult = Library.ExecQuery(sql)
        for i in range(0,len(borrowresult)):
            for j in range(0,len(borrowresult[0])):
                self.borrowedQueryModel.setItem(i, j, QStandardItem(str(borrowresult[i][j])))
        #self.borrowedQueryModel = QStandardItemModel(12,12)
        #self.borrowedQueryModel.setItem(row, column, QStandardItem(data))


        #self.borrowedQueryModel.setQuery(sql)
        return

    def returnedQuery(self):
        sql = f"SELECT * FROM TB_Borrow WHERE rdID={self.studentId} AND IsHasReturn=1"
        Library = MSSQL('Library')
        returnresult = Library.ExecQuery(sql)
        for i in range(0,len(returnresult)):
            for j in range(0,len(returnresult[0])):
                self.returnedQueryModel.setItem(i, j, QStandardItem(str(returnresult[i][j])))
        #print(returnresult)
        
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/MainWindow_1.png"))
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    #mainMindow = BorrowStatusViewer("1")
    #mainMindow.show()
    sys.exit(app.exec_())
