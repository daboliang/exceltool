# -*- coding: utf-8 -*-
import sys  # sys模块提供对Python解释器使用或维护的一些变量的访问，以及与解释器交互的函数。
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口的尺寸
    w.resize(400, 200)
    # 移动窗口
    w.move(900, 300)
    # 设置窗口的标题
    w.setWindowTitle('第一个桌面应用')
    # 显示窗口
    w.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束
    sys.exit(app.exec())


"""
@Time        : 2021/10/2
@Author      : 89464
@File        : test
@Description :
"""
