# -*- coding: utf-8 -*-
import sys
import MainWinverticalLayout

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = MainWinverticalLayout.Ui_MainWindow()
    #  向主窗口上添加控件D
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())

"""
@Time        : 2021/10/5
@Author      : 89464
@File        : layout
@Description : 
"""