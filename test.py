# -*- coding: utf-8 -*-
import sys  # sys模块提供对Python解释器使用或维护的一些变量的访问，以及与解释器交互的函数。
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon


class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 250)
        # 设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')

        # 设置窗口的尺寸
        self.resize(400, 300)

        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的信息', 5000)


if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon('./dog.jpg'))
    main = FirstMainWin()
    main.show()

    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec())


"""
@Time        : 2021/10/2
@Author      : 89464
@File        : test
@Description :
"""
